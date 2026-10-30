import os
from pathlib import Path
from dotenv import load_dotenv
from pinecone import Pinecone

project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("fde-sop-index-local")

print(index.describe_index_stats())