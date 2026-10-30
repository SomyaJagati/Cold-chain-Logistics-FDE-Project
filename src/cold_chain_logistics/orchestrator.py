import sys
from pathlib import Path
from typing import Annotated, TypedDict

from dotenv import load_dotenv

from langchain_core.messages import BaseMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parents[1]

if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

load_dotenv(project_root / ".env")

from src.cold_chain_logistics.agent_tools import (
    query_telemetry_db,
    fetch_corridor_conditions,
    search_compliance_sop
)

prompt_path = project_root / "src" / "prompts" / "system_prompt.txt"

try:
    with open(prompt_path, "r", encoding="utf-8") as f:
        system_instructions = f.read()
except FileNotFoundError:
    raise FileNotFoundError(f"System prompt not found: {prompt_path}")

system_prompt = SystemMessage(content=system_instructions)


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)

fde_tools = [
    query_telemetry_db,
    fetch_corridor_conditions,
    search_compliance_sop
]

llm_with_tools = llm.bind_tools(fde_tools)


def reasoning_node(state: AgentState):
    messages = state["messages"]

    if not any(isinstance(msg, SystemMessage) for msg in messages):
        messages = [system_prompt] + messages

    response = llm_with_tools.invoke(messages)

    return {"messages": [response]}


print("Compiling LangGraph FDE Orchestrator...")

graph_builder = StateGraph(AgentState)

graph_builder.add_node("reasoner", reasoning_node)
graph_builder.add_node("tools", ToolNode(fde_tools))

graph_builder.add_edge(START, "reasoner")

graph_builder.add_conditional_edges(
    "reasoner",
    tools_condition
)

graph_builder.add_edge("tools", "reasoner")

fde_agent = graph_builder.compile(
    checkpointer=MemorySaver()
)


if __name__ == "__main__":

    print("\n" + "=" * 55)
    print("FDE Supply Chain Orchestrator State Machine Online")
    print("=" * 55)

    thread_config = {
        "configurable": {
            "thread_id": "production_test_1"
        }
    }

    while True:

        user_input = input("\nDispatcher > ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Shutting down FDE Orchestrator...")
            break

        if not user_input:
            continue

        try:

            events = fde_agent.stream(
                {"messages": [("user", user_input)]},
                config=thread_config,
                stream_mode="updates"
            )

            for event in events:

                for node_name, node_state in event.items():

                    if node_name == "tools":
                        print(
                            "\n[System] Retrieving external data "
                            "through ToolNode..."
                        )

                    elif node_name == "reasoner":

                        latest_msg = node_state["messages"][-1]

                        if latest_msg.content:
                            print(f"\nFDE Agent:\n{latest_msg.content}")

        except Exception as e:
            print(f"\nAgent Error: {e}")

