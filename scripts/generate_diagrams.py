"""
Generates high-definition, professional SVG diagrams for Cold Chain Logistics architecture.
Output directory: docs/images/
"""

from pathlib import Path

def create_hld_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="100%" height="100%" style="background:#090D16; font-family:'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <defs>
    <linearGradient id="gradBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#090D16" />
    </linearGradient>
    <linearGradient id="gradBlue" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#0284C7" />
    </linearGradient>
    <linearGradient id="gradPurple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A855F7" />
      <stop offset="100%" stop-color="#7C3AED" />
    </linearGradient>
    <linearGradient id="gradGreen" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#059669" />
    </linearGradient>
    <linearGradient id="gradOrange" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#38BDF8"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#10B981"/>
    </marker>
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#A855F7"/>
    </marker>
  </defs>

  <!-- Title Badge -->
  <rect x="40" y="25" width="1020" height="55" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1.5" filter="url(#glow)"/>
  <circle cx="70" cy="52" r="14" fill="#38BDF8" fill-opacity="0.2"/>
  <text x="70" y="58" text-anchor="middle" font-size="16" fill="#38BDF8">🧊</text>
  <text x="95" y="50" font-size="18" font-weight="700" fill="#F8FAFC">COLD CHAIN LOGISTICS PLATFORM - SYSTEM ARCHITECTURE (HLD)</text>
  <text x="95" y="68" font-size="12" fill="#94A3B8">High-Level Design • Multi-Source AI Agentic Dispatch &amp; Telemetry Decision System</text>

  <!-- USER / DISPATCHER LAYER -->
  <rect x="40" y="110" width="220" height="520" rx="12" fill="#111827" stroke="#1F2937" stroke-width="1.5"/>
  <rect x="55" y="125" width="190" height="32" rx="6" fill="#1F2937"/>
  <text x="150" y="146" text-anchor="middle" font-size="13" font-weight="700" fill="#38BDF8">PRESENTATION LAYER</text>

  <rect x="55" y="180" width="190" height="110" rx="8" fill="#1E293B" stroke="#334155" filter="url(#glow)"/>
  <text x="70" y="208" font-size="20">👤</text>
  <text x="98" y="205" font-size="14" font-weight="700" fill="#F1F5F9">Fleet Dispatcher</text>
  <text x="70" y="230" font-size="11" fill="#94A3B8">• Natural Language Queries</text>
  <text x="70" y="248" font-size="11" fill="#94A3B8">• Anomaly &amp; Breach Analysis</text>
  <text x="70" y="266" font-size="11" fill="#94A3B8">• Mitigation Approvals</text>

  <rect x="55" y="320" width="190" height="280" rx="8" fill="#1E293B" stroke="#334155" filter="url(#glow)"/>
  <rect x="70" y="335" width="160" height="28" rx="5" fill="#38BDF8" fill-opacity="0.15"/>
  <text x="150" y="353" text-anchor="middle" font-size="12" font-weight="700" fill="#38BDF8">Streamlit Console HUD</text>
  <text x="70" y="385" font-size="11" font-weight="600" fill="#E2E8F0">🧭 Dispatch View</text>
  <text x="75" y="403" font-size="10" fill="#94A3B8">- Live Telemetry Inspection</text>
  <text x="75" y="419" font-size="10" fill="#94A3B8">- Real-Time Tool Execution Trace</text>
  <text x="75" y="435" font-size="10" fill="#94A3B8">- Structured SOP Citations</text>
  <path d="M 70 450 L 230 450" stroke="#334155" stroke-width="1"/>
  <text x="70" y="475" font-size="11" font-weight="600" fill="#10B981">🛡️ Audit Log Viewer</text>
  <text x="75" y="493" font-size="10" fill="#94A3B8">- Admin Credential Gate</text>
  <text x="75" y="509" font-size="10" fill="#94A3B8">- Immutable Execution Trace</text>
  <text x="75" y="525" font-size="10" fill="#94A3B8">- Node &amp; Tool Payload Audits</text>
  <text x="75" y="555" font-size="10" fill="#F59E0B">⚡ UUID Thread Sessioning</text>
  <text x="75" y="571" font-size="10" fill="#94A3B8">- Isolated memory persistence</text>

  <!-- AGENTIC ORCHESTRATION LAYER -->
  <rect x="300" y="110" width="370" height="520" rx="12" fill="#111827" stroke="#1F2937" stroke-width="1.5"/>
  <rect x="320" y="125" width="330" height="32" rx="6" fill="#1F2937"/>
  <text x="485" y="146" text-anchor="middle" font-size="13" font-weight="700" fill="#A855F7">AGENT ORCHESTRATION LAYER</text>

  <rect x="320" y="180" width="330" height="150" rx="10" fill="#1E293B" stroke="#475569" filter="url(#glow)"/>
  <rect x="335" y="195" width="300" height="26" rx="5" fill="#A855F7" fill-opacity="0.2"/>
  <text x="485" y="213" text-anchor="middle" font-size="12" font-weight="700" fill="#C084FC">LangGraph State Machine Engine</text>
  <text x="340" y="245" font-size="11" fill="#E2E8F0"><tspan font-weight="bold" fill="#38BDF8">• Reasoner Node:</tspan> Google Gemini 3.8 Flash</text>
  <text x="340" y="265" font-size="11" fill="#E2E8F0"><tspan font-weight="bold" fill="#F59E0B">• Memory Saver:</tspan> Multi-Turn Thread Checkpointer</text>
  <text x="340" y="285" font-size="11" fill="#E2E8F0"><tspan font-weight="bold" fill="#10B981">• ToolNode Router:</tspan> Conditional Re-act Looping</text>
  <text x="340" y="305" font-size="11" fill="#E2E8F0"><tspan font-weight="bold" fill="#EC4899">• System Prompt:</tspan> Senior Logistics Scientist Persona</text>

  <!-- TOOL NODES BOX -->
  <rect x="320" y="355" width="330" height="250" rx="10" fill="#1E1B4B" stroke="#4338CA" filter="url(#glow)"/>
  <text x="485" y="380" text-anchor="middle" font-size="12" font-weight="700" fill="#A5B4FC">Tool Node Bindings (LangChain Tools)</text>

  <!-- Tool 1 -->
  <rect x="335" y="395" width="300" height="60" rx="6" fill="#1E293B" stroke="#334155"/>
  <text x="345" y="416" font-size="12" font-weight="700" fill="#38BDF8">query_telemetry_db(sql_query)</text>
  <text x="345" y="433" font-size="10" fill="#94A3B8">• Validates SELECT-only queries</text>
  <text x="345" y="446" font-size="10" fill="#94A3B8">• Targets FDE_VIEWS.VW_ACTIVE_FLEET via pyodbc</text>

  <!-- Tool 2 -->
  <rect x="335" y="465" width="300" height="60" rx="6" fill="#1E293B" stroke="#334155"/>
  <text x="345" y="486" font-size="12" font-weight="700" fill="#F59E0B">fetch_corridor_conditions(lat, lon)</text>
  <text x="345" y="503" font-size="10" fill="#94A3B8">• GPS reverse coordinate querying</text>
  <text x="345" y="516" font-size="10" fill="#94A3B8">• Real-time wind, ambient temp &amp; congestion</text>

  <!-- Tool 3 -->
  <rect x="335" y="535" width="300" height="60" rx="6" fill="#1E293B" stroke="#334155"/>
  <text x="345" y="556" font-size="12" font-weight="700" fill="#10B981">search_compliance_sop(query)</text>
  <text x="345" y="573" font-size="10" fill="#94A3B8">• Semantic Vector Search over Cold Chain SOPs</text>
  <text x="345" y="586" font-size="10" fill="#94A3B8">• Returns threshold breach mitigation rules</text>

  <!-- DATA & SUBSYSTEM LAYER -->
  <rect x="710" y="110" width="350" height="520" rx="12" fill="#111827" stroke="#1F2937" stroke-width="1.5"/>
  <rect x="730" y="125" width="310" height="32" rx="6" fill="#1F2937"/>
  <text x="885" y="146" text-anchor="middle" font-size="13" font-weight="700" fill="#10B981">DATA &amp; INFRASTRUCTURE LAYER</text>

  <!-- Database Box -->
  <rect x="730" y="175" width="310" height="185" rx="8" fill="#1E293B" stroke="#334155" filter="url(#glow)"/>
  <rect x="745" y="188" width="280" height="24" rx="4" fill="#0284C7" fill-opacity="0.2"/>
  <text x="885" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#38BDF8">Enterprise MS SQL Server 2022 (Docker)</text>
  
  <rect x="745" y="220" width="280" height="60" rx="5" fill="#0F172A" stroke="#1E293B"/>
  <text x="755" y="238" font-size="11" font-weight="700" fill="#10B981">FDE_VIEWS Schema (Curated Semantic Layer)</text>
  <text x="755" y="254" font-size="10" fill="#94A3B8">• VW_ACTIVE_FLEET (Clean Aliases &amp; Cast Types)</text>
  <text x="755" y="268" font-size="10" fill="#94A3B8">• AgentAuditLog (State &amp; Tool Audit Store)</text>

  <rect x="745" y="288" width="280" height="60" rx="5" fill="#450A0A" stroke="#7F1D1D"/>
  <text x="755" y="306" font-size="11" font-weight="700" fill="#EF4444">dbo.TBL_SC_FLEET_HIST_RAW (Locked)</text>
  <text x="755" y="322" font-size="10" fill="#FCA5A5">• Cryptic columns: TS_UTC, V_LAT, IOT_TEMP_VAL_C</text>
  <text x="755" y="336" font-size="10" fill="#EF4444">• AGENT ACCESS STRICTLY DENIED (Zero-Trust)</text>

  <!-- External Weather API -->
  <rect x="730" y="375" width="310" height="95" rx="8" fill="#1E293B" stroke="#334155" filter="url(#glow)"/>
  <rect x="745" y="388" width="280" height="24" rx="4" fill="#D97706" fill-opacity="0.2"/>
  <text x="885" y="405" text-anchor="middle" font-size="11" font-weight="700" fill="#F59E0B">Open-Meteo REST API (Live Weather)</text>
  <text x="750" y="432" font-size="10" fill="#CBD5E1">• Real-Time Ambient Temperature (°C)</text>
  <text x="750" y="448" font-size="10" fill="#CBD5E1">• Wind Speed &amp; Calculated Corridor Congestion Index</text>
  <text x="750" y="462" font-size="10" fill="#94A3B8">• Non-cached live satellite &amp; ground station feed</text>

  <!-- Pinecone Vector Store -->
  <rect x="730" y="485" width="310" height="135" rx="8" fill="#1E293B" stroke="#334155" filter="url(#glow)"/>
  <rect x="745" y="498" width="280" height="24" rx="4" fill="#059669" fill-opacity="0.2"/>
  <text x="885" y="515" text-anchor="middle" font-size="11" font-weight="700" fill="#34D399">Pinecone Vector DB (Serverless)</text>
  <text x="750" y="542" font-size="10" fill="#CBD5E1">• Index: fde-sop-index-local (1024 Dim, Cosine)</text>
  <text x="750" y="558" font-size="10" fill="#CBD5E1">• Embeddings: BAAI/bge-m3 (Local CPU Caching)</text>
  <text x="750" y="574" font-size="10" fill="#CBD5E1">• Incremental Ingestion &amp; MD5 Hash Cache</text>
  <text x="750" y="590" font-size="10" fill="#94A3B8">• Cold-Chain Breach SOPs &amp; Rerouting Protocols</text>

  <!-- INTERCONNECTING ARROWS -->
  <!-- Streamlit to Orchestrator -->
  <path d="M 245 235 L 320 235" stroke="#38BDF8" stroke-width="2" marker-end="url(#arrow)"/>
  <path d="M 320 260 L 245 260" stroke="#A855F7" stroke-width="2" marker-end="url(#arrow-purple)"/>

  <!-- Orchestrator to Tools -->
  <path d="M 485 330 L 485 355" stroke="#A855F7" stroke-width="2" marker-end="url(#arrow-purple)"/>

  <!-- Tool 1 to SQL Server -->
  <path d="M 635 425 L 680 425 L 680 250 L 730 250" stroke="#38BDF8" stroke-width="2" fill="none" marker-end="url(#arrow)"/>

  <!-- Tool 2 to Weather API -->
  <path d="M 635 495 L 690 495 L 690 420 L 730 420" stroke="#F59E0B" stroke-width="2" fill="none" marker-end="url(#arrow)"/>

  <!-- Tool 3 to Pinecone -->
  <path d="M 635 565 L 730 565" stroke="#10B981" stroke-width="2" fill="none" marker-end="url(#arrow-green)"/>

  <!-- Audit Log Link back to UI -->
  <path d="M 745 270 L 705 270 L 705 520 L 245 520" stroke="#10B981" stroke-width="1.5" stroke-dasharray="4" fill="none" marker-end="url(#arrow-green)"/>
</svg>
"""

def create_lld_orchestration_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700" width="100%" height="100%" style="background:#090D16; font-family:'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <defs>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
    <marker id="arr-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#38BDF8"/>
    </marker>
    <marker id="arr-purple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#C084FC"/>
    </marker>
    <marker id="arr-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#34D399"/>
    </marker>
    <marker id="arr-orange" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#FBBF24"/>
    </marker>
  </defs>

  <!-- Title Header -->
  <rect x="40" y="20" width="1020" height="55" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
  <circle cx="70" cy="47" r="14" fill="#C084FC" fill-opacity="0.2"/>
  <text x="70" y="53" text-anchor="middle" font-size="16" fill="#C084FC">⚡</text>
  <text x="95" y="45" font-size="18" font-weight="700" fill="#F8FAFC">AGENT ORCHESTRATION STATE MACHINE (LLD)</text>
  <text x="95" y="63" font-size="12" fill="#94A3B8">Low-Level Design • LangGraph StateGraph, Tool Routing &amp; Domino-Effect Multi-Tool Synthesis</text>

  <!-- User Input Step -->
  <rect x="40" y="100" width="220" height="90" rx="10" fill="#1E293B" stroke="#38BDF8" stroke-width="2" filter="url(#shadow)"/>
  <text x="60" y="125" font-size="13" font-weight="700" fill="#38BDF8">START / USER DISPATCH</text>
  <text x="60" y="145" font-size="11" fill="#E2E8F0">HumanMessage(content)</text>
  <text x="60" y="162" font-size="10" fill="#94A3B8">e.g. "Shipments in LA with high risk;</text>
  <text x="60" y="176" font-size="10" fill="#94A3B8">check weather &amp; SOP breach"</text>

  <!-- State Container -->
  <rect x="40" y="225" width="220" height="150" rx="10" fill="#111827" stroke="#334155" filter="url(#shadow)"/>
  <rect x="55" y="238" width="190" height="24" rx="4" fill="#1F2937"/>
  <text x="150" y="254" text-anchor="middle" font-size="11" font-weight="700" fill="#38BDF8">AgentState (TypedDict)</text>
  <text x="55" y="280" font-size="11" fill="#E2E8F0"><tspan font-weight="bold">messages:</tspan> Annotated[</text>
  <text x="70" y="296" font-size="10" fill="#94A3B8">list[BaseMessage],</text>
  <text x="70" y="312" font-size="10" fill="#94A3B8">add_messages</text>
  <text x="55" y="328" font-size="11" fill="#E2E8F0">]</text>
  <text x="55" y="350" font-size="10" fill="#F59E0B">Checkpointer: MemorySaver</text>
  <text x="55" y="364" font-size="10" fill="#94A3B8">Thread-isolated context</text>

  <!-- Arrow to Reasoner -->
  <path d="M 260 145 L 340 145" stroke="#38BDF8" stroke-width="2" marker-end="url(#arr-blue)"/>

  <!-- REASONER NODE -->
  <rect x="340" y="90" width="340" height="230" rx="12" fill="#1E1B4B" stroke="#6366F1" stroke-width="2" filter="url(#shadow)"/>
  <rect x="360" y="105" width="300" height="28" rx="6" fill="#4338CA"/>
  <text x="510" y="124" text-anchor="middle" font-size="13" font-weight="700" fill="#EEF2FF">NODE: reasoner (Gemini 3.8 Flash)</text>

  <text x="360" y="155" font-size="11" fill="#E0E7FF"><tspan font-weight="bold">1. Inject Persona:</tspan> SystemMessage</text>
  <text x="375" y="170" font-size="10" fill="#A5B4FC">• Senior Logistics Data Scientist instructions</text>
  <text x="375" y="184" font-size="10" fill="#A5B4FC">• Strictly mandates 3-part structured business response</text>

  <text x="360" y="208" font-size="11" fill="#E0E7FF"><tspan font-weight="bold">2. Tool Binding:</tspan> llm.bind_tools(fde_tools)</text>
  <text x="375" y="223" font-size="10" fill="#A5B4FC">• Evaluates query against function signatures</text>
  <text x="375" y="237" font-size="10" fill="#A5B4FC">• Generates tool arguments (SQL, GPS coordinates, queries)</text>

  <text x="360" y="262" font-size="11" fill="#E0E7FF"><tspan font-weight="bold">3. Re-act Evaluation &amp; Convergence:</tspan></text>
  <text x="375" y="277" font-size="10" fill="#A5B4FC">• Loops until all operational context is fulfilled</text>
  <text x="375" y="291" font-size="10" fill="#A5B4FC">• Formats Executive Summary, Telemetry Table &amp; SOP Plan</text>
  <text x="375" y="305" font-size="10" fill="#10B981">• Silently dispatches trace to AgentAuditLog</text>

  <!-- Conditional Edge: tools_condition -->
  <path d="M 510 320 L 510 375" stroke="#C084FC" stroke-width="2" marker-end="url(#arr-purple)"/>

  <polygon points="510,380 580,420 510,460 440,420" fill="#1E293B" stroke="#F59E0B" stroke-width="2" filter="url(#shadow)"/>
  <text x="510" y="416" text-anchor="middle" font-size="11" font-weight="700" fill="#FBBF24">tools_condition</text>
  <text x="510" y="430" text-anchor="middle" font-size="9" fill="#E2E8F0">Has Tool Calls?</text>

  <!-- Route to END -->
  <path d="M 580 420 L 760 420 L 760 270" stroke="#10B981" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>
  <text x="660" y="412" font-size="11" font-weight="700" fill="#10B981">[False: Done]</text>

  <!-- Route to TOOLS -->
  <path d="M 510 460 L 510 510" stroke="#38BDF8" stroke-width="2" marker-end="url(#arr-blue)"/>
  <text x="520" y="485" font-size="11" font-weight="700" fill="#38BDF8">[True: Invoke Tools]</text>

  <!-- TOOLNODE -->
  <rect x="220" y="510" width="580" height="165" rx="12" fill="#0F172A" stroke="#38BDF8" stroke-width="2" filter="url(#shadow)"/>
  <rect x="240" y="522" width="540" height="26" rx="6" fill="#0284C7" fill-opacity="0.25"/>
  <text x="510" y="540" text-anchor="middle" font-size="12" font-weight="700" fill="#38BDF8">NODE: tools (ToolNode Execution Subsystem)</text>

  <!-- 3 Parallel / Sequenced Tools -->
  <rect x="240" y="560" width="165" height="100" rx="8" fill="#1E293B" stroke="#334155"/>
  <text x="250" y="580" font-size="11" font-weight="700" fill="#38BDF8">1. query_telemetry_db</text>
  <text x="250" y="598" font-size="9" fill="#94A3B8">• Generates T-SQL query</text>
  <text x="250" y="612" font-size="9" fill="#94A3B8">• Validates SELECT-only</text>
  <text x="250" y="626" font-size="9" fill="#94A3B8">• Queries VW_ACTIVE_FLEET</text>
  <text x="250" y="640" font-size="9" fill="#94A3B8">• Returns Lat, Lon, Temp, Risk</text>

  <rect x="420" y="560" width="180" height="100" rx="8" fill="#1E293B" stroke="#334155"/>
  <text x="430" y="580" font-size="11" font-weight="700" fill="#F59E0B">2. fetch_corridor_conditions</text>
  <text x="430" y="598" font-size="9" fill="#94A3B8">• Takes (Latitude, Longitude)</text>
  <text x="430" y="612" font-size="9" fill="#94A3B8">• Calls Open-Meteo REST API</text>
  <text x="430" y="626" font-size="9" fill="#94A3B8">• Fetches Ambient Temp &amp; Wind</text>
  <text x="430" y="640" font-size="9" fill="#94A3B8">• Computes Congestion Index</text>

  <rect x="615" y="560" width="170" height="100" rx="8" fill="#1E293B" stroke="#334155"/>
  <text x="625" y="580" font-size="11" font-weight="700" fill="#10B981">3. search_compliance_sop</text>
  <text x="625" y="598" font-size="9" fill="#94A3B8">• Pinecone Vector Retrieval</text>
  <text x="625" y="612" font-size="9" fill="#94A3B8">• Top-k=2 SOP Clauses</text>
  <text x="625" y="626" font-size="9" fill="#94A3B8">• Identifies 4.0°C Breaches</text>
  <text x="625" y="640" font-size="9" fill="#94A3B8">• Cites diversion to depot</text>

  <!-- Loop back from Tools to Reasoner -->
  <path d="M 220 590 L 180 590 L 180 200 L 340 200" stroke="#C084FC" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>
  <text x="190" y="450" font-size="11" font-weight="700" fill="#C084FC" transform="rotate(-90 190,450)">Returns ToolMessage Payloads</text>

  <!-- END NODE & OUTPUT SYNTHESIS -->
  <rect x="760" y="90" width="300" height="230" rx="12" fill="#064E3B" stroke="#10B981" stroke-width="2" filter="url(#shadow)"/>
  <rect x="780" y="105" width="260" height="28" rx="6" fill="#047857"/>
  <text x="910" y="124" text-anchor="middle" font-size="13" font-weight="700" fill="#ECFDF5">END: STRUCTURED BUSINESS REPORT</text>

  <rect x="780" y="145" width="260" height="42" rx="4" fill="#022C22"/>
  <text x="790" y="162" font-size="11" font-weight="700" fill="#34D399">1. Executive Summary</text>
  <text x="790" y="176" font-size="9" fill="#A7F3D0">Concise anomaly, risk magnitude, immediate alert</text>

  <rect x="780" y="195" width="260" height="42" rx="4" fill="#022C22"/>
  <text x="790" y="212" font-size="11" font-weight="700" fill="#34D399">2. Telemetry &amp; Environment Table</text>
  <text x="790" y="226" font-size="9" fill="#A7F3D0">Lat/Lon | Current Temp | Cargo Risk | Wind/Corridor</text>

  <rect x="780" y="245" width="260" height="58" rx="4" fill="#022C22"/>
  <text x="790" y="262" font-size="11" font-weight="700" fill="#34D399">3. Required Action Plan &amp; Citations</text>
  <text x="790" y="278" font-size="9" fill="#A7F3D0">• Immediate Step: Auxiliary cooling restart</text>
  <text x="790" y="292" font-size="9" fill="#A7F3D0">• SOP Citation: SOP v2.4 Section 1 (Fresh Perishables)</text>

  <!-- UI Stream Output -->
  <path d="M 910 320 L 910 490 L 820 490" stroke="#10B981" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>
  <rect x="820" y="470" width="240" height="100" rx="8" fill="#1E293B" stroke="#334155" filter="url(#shadow)"/>
  <text x="835" y="495" font-size="12" font-weight="700" fill="#F8FAFC">Streamlit Real-Time Stream</text>
  <text x="835" y="515" font-size="10" fill="#94A3B8">• Streaming token-by-token output</text>
  <text x="835" y="530" font-size="10" fill="#94A3B8">• Collapsible tool inspect accordions</text>
  <text x="835" y="545" font-size="10" fill="#94A3B8">• Background SQL audit injection</text>
</svg>
"""

def create_lld_data_security_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700" width="100%" height="100%" style="background:#090D16; font-family:'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <defs>
    <filter id="glow-sec" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
    <marker id="arr-red" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#EF4444"/>
    </marker>
    <marker id="arr-green-sec" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#10B981"/>
    </marker>
    <marker id="arr-blue-sec" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#38BDF8"/>
    </marker>
  </defs>

  <!-- Title Header -->
  <rect x="40" y="20" width="1020" height="55" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1.5" filter="url(#glow-sec)"/>
  <circle cx="70" cy="47" r="14" fill="#10B981" fill-opacity="0.2"/>
  <text x="70" y="53" text-anchor="middle" font-size="16" fill="#10B981">🛡️</text>
  <text x="95" y="45" font-size="18" font-weight="700" fill="#F8FAFC">DATA &amp; SECURITY MODEL ARCHITECTURE (LLD)</text>
  <text x="95" y="63" font-size="12" fill="#94A3B8">Low-Level Design • Semantic Schema Abstraction, Strict RBAC Isolation &amp; Audit Trail</text>

  <!-- LEFT COLUMN: PRINCIPALS & ROLES -->
  <rect x="40" y="100" width="280" height="565" rx="12" fill="#111827" stroke="#1F2937" stroke-width="1.5"/>
  <rect x="55" y="115" width="250" height="30" rx="6" fill="#1F2937"/>
  <text x="180" y="135" text-anchor="middle" font-size="13" font-weight="700" fill="#38BDF8">SECURITY PRINCIPALS (RBAC)</text>

  <!-- Principal 1: USR_FDE_RO (Agent) -->
  <rect x="55" y="165" width="250" height="190" rx="10" fill="#1E293B" stroke="#38BDF8" filter="url(#glow-sec)"/>
  <rect x="70" y="178" width="220" height="24" rx="4" fill="#0284C7" fill-opacity="0.2"/>
  <text x="180" y="195" text-anchor="middle" font-size="12" font-weight="700" fill="#38BDF8">🤖 Agent Principal (USR_FDE_RO)</text>
  
  <text x="70" y="225" font-size="11" font-weight="700" fill="#10B981">PERMISSIONS GRANTED:</text>
  <text x="75" y="243" font-size="10" fill="#CBD5E1">✓ GRANT SELECT ON</text>
  <text x="85" y="258" font-size="10" fill="#38BDF8">FDE_VIEWS.VW_ACTIVE_FLEET</text>
  <text x="75" y="278" font-size="10" fill="#CBD5E1">✓ GRANT INSERT ON</text>
  <text x="85" y="293" font-size="10" fill="#38BDF8">FDE_VIEWS.AgentAuditLog</text>

  <text x="70" y="318" font-size="11" font-weight="700" fill="#EF4444">PERMISSIONS DENIED:</text>
  <text x="75" y="335" font-size="10" fill="#FCA5A5">✗ DENY SELECT ON dbo.TBL_SC_FLEET_HIST_RAW</text>
  <text x="75" y="349" font-size="10" fill="#FCA5A5">✗ DENY INSERT, UPDATE, DELETE ON dbo.*</text>

  <!-- Principal 2: SQL_ADMIN_USER -->
  <rect x="55" y="375" width="250" height="150" rx="10" fill="#1E293B" stroke="#F59E0B" filter="url(#glow-sec)"/>
  <rect x="70" y="388" width="220" height="24" rx="4" fill="#D97706" fill-opacity="0.2"/>
  <text x="180" y="405" text-anchor="middle" font-size="12" font-weight="700" fill="#FBBF24">🔑 Admin Principal (sa / Admin)</text>
  
  <text x="70" y="435" font-size="10" fill="#CBD5E1">• High-privilege database owner</text>
  <text x="70" y="452" font-size="10" fill="#CBD5E1">• Performs initial schema migrations &amp; DDL</text>
  <text x="70" y="469" font-size="10" fill="#CBD5E1">• Enforces user isolation policies</text>
  <text x="70" y="486" font-size="10" fill="#CBD5E1">• Authenticates Streamlit Audit Inspector</text>
  <text x="70" y="503" font-size="10" fill="#CBD5E1">• Full SELECT access on AgentAuditLog</text>

  <!-- App-Level Security Gate -->
  <rect x="55" y="545" width="250" height="105" rx="8" fill="#1E1B4B" stroke="#6366F1"/>
  <text x="70" y="568" font-size="11" font-weight="700" fill="#A5B4FC">Application-Level Guardrails</text>
  <text x="70" y="588" font-size="10" fill="#CBD5E1">• RegEx: query.strip().startswith('SELECT')</text>
  <text x="70" y="605" font-size="10" fill="#CBD5E1">• Result Limiter: fetchmany(10) (No DoS)</text>
  <text x="70" y="622" font-size="10" fill="#CBD5E1">• Parameterized DB Connection Strings</text>
  <text x="70" y="639" font-size="10" fill="#CBD5E1">• Zero Raw Credentials in System Prompts</text>

  <!-- CENTER COLUMN: SQL SCHEMA TRANSFORMATION -->
  <rect x="360" y="100" width="370" height="565" rx="12" fill="#111827" stroke="#1F2937" stroke-width="1.5"/>
  <rect x="380" y="115" width="330" height="30" rx="6" fill="#1F2937"/>
  <text x="545" y="135" text-anchor="middle" font-size="13" font-weight="700" fill="#10B981">DATABASE SCHEMA &amp; SEMANTIC LAYER</text>

  <!-- Clean Semantic View -->
  <rect x="380" y="165" width="330" height="230" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="2" filter="url(#glow-sec)"/>
  <rect x="395" y="178" width="300" height="26" rx="4" fill="#059669" fill-opacity="0.25"/>
  <text x="545" y="196" text-anchor="middle" font-size="12" font-weight="700" fill="#34D399">FDE_VIEWS.VW_ACTIVE_FLEET (Semantic View)</text>

  <text x="395" y="225" font-size="10" font-weight="700" fill="#94A3B8">CLEAN COLUMN NAME</text>
  <text x="555" y="225" font-size="10" font-weight="700" fill="#94A3B8">MAPPED LEGACY SOURCE</text>

  <text x="395" y="246" font-size="10" fill="#38BDF8">Timestamp</text>
  <text x="555" y="246" font-size="10" fill="#64748B">TS_UTC (DateTime)</text>

  <text x="395" y="264" font-size="10" fill="#38BDF8">Latitude, Longitude</text>
  <text x="555" y="264" font-size="10" fill="#64748B">V_LAT, V_LON (Float)</text>

  <text x="395" y="282" font-size="10" fill="#38BDF8">Current_Temperature_C</text>
  <text x="555" y="282" font-size="10" fill="#64748B">CAST(IOT_TEMP_VAL_C AS FLOAT)</text>

  <text x="395" y="300" font-size="10" fill="#38BDF8">Cargo_Condition_Code</text>
  <text x="555" y="300" font-size="10" fill="#64748B">CGO_COND_CD</text>

  <text x="395" y="318" font-size="10" fill="#38BDF8">Risk_Classification</text>
  <text x="555" y="318" font-size="10" fill="#64748B">RISK_CLS_TXT</text>

  <text x="395" y="336" font-size="10" fill="#38BDF8">Delay_Probability</text>
  <text x="555" y="336" font-size="10" fill="#64748B">DELAY_PROB_DEC</text>

  <text x="395" y="354" font-size="10" fill="#38BDF8">Port_Congestion_Level</text>
  <text x="555" y="354" font-size="10" fill="#64748B">PRT_CNG_LVL</text>

  <text x="395" y="372" font-size="10" fill="#38BDF8">Route_Risk_Index</text>
  <text x="555" y="372" font-size="10" fill="#64748B">RT_RSK_IDX</text>

  <!-- Legacy Table (Blocked) -->
  <rect x="380" y="420" width="330" height="110" rx="10" fill="#450A0A" stroke="#DC2626" stroke-width="2" filter="url(#glow-sec)"/>
  <rect x="395" y="432" width="300" height="24" rx="4" fill="#7F1D1D"/>
  <text x="545" y="449" text-anchor="middle" font-size="12" font-weight="700" fill="#FCA5A5">🚫 dbo.TBL_SC_FLEET_HIST_RAW (Raw Table)</text>

  <text x="395" y="475" font-size="10" fill="#FECACA">• Unclean legacy naming conventions (TS_UTC, V_LAT)</text>
  <text x="395" y="492" font-size="10" fill="#FECACA">• Contains internal tracking flag (SYS_INGEST_FLAG)</text>
  <text x="395" y="509" font-size="10" font-weight="700" fill="#EF4444">• DIRECT ACCESS DENIED TO AGENT LOGIN (Hard Security Boundary)</text>

  <!-- Audit Table -->
  <rect x="380" y="550" width="330" height="100" rx="8" fill="#1E293B" stroke="#475569"/>
  <text x="395" y="572" font-size="11" font-weight="700" fill="#38BDF8">FDE_VIEWS.AgentAuditLog</text>
  <text x="395" y="590" font-size="10" fill="#CBD5E1">• Columns: LogID (PK), Timestamp, SessionID,</text>
  <text x="395" y="605" font-size="10" fill="#CBD5E1">  NodeExecuted, ToolName, Content (NVARCHAR(MAX))</text>
  <text x="395" y="622" font-size="10" fill="#10B981">• USR_FDE_RO has INSERT privilege only</text>
  <text x="395" y="638" font-size="10" fill="#F59E0B">• Admin has SELECT privilege to review forensics</text>

  <!-- RIGHT COLUMN: VECTOR STORE & POLICY RAG -->
  <rect x="770" y="100" width="290" height="565" rx="12" fill="#111827" stroke="#1F2937" stroke-width="1.5"/>
  <rect x="790" y="115" width="250" height="30" rx="6" fill="#1F2937"/>
  <text x="915" y="135" text-anchor="middle" font-size="13" font-weight="700" fill="#A855F7">VECTOR KNOWLEDGE &amp; RAG</text>

  <!-- Vector Store Spec -->
  <rect x="790" y="165" width="250" height="230" rx="10" fill="#1E293B" stroke="#8B5CF6" filter="url(#glow-sec)"/>
  <rect x="805" y="178" width="220" height="24" rx="4" fill="#6D28D9" fill-opacity="0.3"/>
  <text x="915" y="195" text-anchor="middle" font-size="12" font-weight="700" fill="#C4B5FD">Pinecone Vector Store</text>

  <text x="805" y="225" font-size="10" fill="#E2E8F0"><tspan font-weight="bold">Index:</tspan> fde-sop-index-local</text>
  <text x="805" y="243" font-size="10" fill="#E2E8F0"><tspan font-weight="bold">Embedding Model:</tspan> BAAI/bge-m3</text>
  <text x="805" y="261" font-size="10" fill="#E2E8F0"><tspan font-weight="bold">Dimension:</tspan> 1024 (Dense vector)</text>
  <text x="805" y="279" font-size="10" fill="#E2E8F0"><tspan font-weight="bold">Metric:</tspan> Cosine Similarity</text>
  <text x="805" y="297" font-size="10" fill="#E2E8F0"><tspan font-weight="bold">Cloud Spec:</tspan> AWS us-east-1 serverless</text>
  <text x="805" y="315" font-size="10" fill="#E2E8F0"><tspan font-weight="bold">Retrieval top-k:</tspan> 2 documents</text>
  <text x="805" y="340" font-size="10" font-weight="700" fill="#34D399">Self-Healing Sync:</text>
  <text x="805" y="356" font-size="9" fill="#94A3B8">• Validates index dimension automatically</text>
  <text x="805" y="370" font-size="9" fill="#94A3B8">• Re-creates index if dimension drifted</text>

  <!-- Ingestion Pipeline -->
  <rect x="790" y="420" width="250" height="230" rx="10" fill="#1E293B" stroke="#334155" filter="url(#glow-sec)"/>
  <text x="805" y="445" font-size="11" font-weight="700" fill="#38BDF8">Idempotent Ingestion Pipeline</text>
  
  <text x="805" y="470" font-size="10" fill="#CBD5E1">1. Polymorphic Parser (.md, .pdf, .csv, .xlsx)</text>
  <text x="805" y="488" font-size="10" fill="#CBD5E1">2. Hierarchical Header &amp; Char Splitter</text>
  <text x="805" y="506" font-size="10" fill="#CBD5E1">3. MD5 State Hashing Cache:</text>
  <text x="815" y="522" font-size="9" fill="#FBBF24">ingestion_hash_cache.json</text>
  <text x="805" y="542" font-size="10" fill="#CBD5E1">4. Zero Duplicate Re-embeddings</text>
  <text x="805" y="560" font-size="10" fill="#CBD5E1">5. Automated Tombstone Purge</text>
  <text x="815" y="576" font-size="9" fill="#94A3B8">• Deletes removed files from Pinecone</text>
  <text x="805" y="598" font-size="10" fill="#CBD5E1">6. Batch Upserting (100 docs / batch)</text>

  <!-- CONNECTIONS / ARROWS -->
  <!-- Agent to Semantic View (ALLOWED) -->
  <path d="M 305 240 L 380 240" stroke="#10B981" stroke-width="2" marker-end="url(#arr-green-sec)"/>
  <text x="315" y="232" font-size="9" font-weight="700" fill="#10B981">SELECT</text>

  <!-- Agent to Raw DB (BLOCKED) -->
  <path d="M 305 340 L 340 340 L 340 470 L 380 470" stroke="#EF4444" stroke-width="2" stroke-dasharray="4" fill="none" marker-end="url(#arr-red)"/>
  <text x="310" y="462" font-size="10" font-weight="700" fill="#EF4444">DENIED</text>

  <!-- Agent to Audit Log (INSERT ONLY) -->
  <path d="M 305 285 L 345 285 L 345 590 L 380 590" stroke="#38BDF8" stroke-width="2" fill="none" marker-end="url(#arr-blue-sec)"/>
  <text x="315" y="582" font-size="9" font-weight="700" fill="#38BDF8">INSERT</text>
</svg>
"""

def main():
    out_dir = Path(__file__).resolve().parent.parent / "docs" / "images"
    out_dir.mkdir(parents=True, exist_ok=True)

    hld_path = out_dir / "system_architecture_hld.svg"
    lld_orch_path = out_dir / "agent_orchestration_lld.svg"
    lld_sec_path = out_dir / "data_security_model_lld.svg"

    hld_path.write_text(create_hld_svg(), encoding="utf-8")
    print(f"Generated: {hld_path}")

    lld_orch_path.write_text(create_lld_orchestration_svg(), encoding="utf-8")
    print(f"Generated: {lld_orch_path}")

    lld_sec_path.write_text(create_lld_data_security_svg(), encoding="utf-8")
    print(f"Generated: {lld_sec_path}")

if __name__ == "__main__":
    main()

