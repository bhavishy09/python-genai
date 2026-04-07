from dotenv import load_dotenv
import os
from pathlib import Path
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from google import genai

# ── config ───────────────────────────────────────────
load_dotenv(Path(__file__).parent / ".env")
api_key = os.getenv("GOOGLE_API_KEY")
client  = genai.Client(api_key=api_key)

# ── connect to existing collection (NO re-embedding) ─
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=api_key
)

vector_store = QdrantVectorStore.from_existing_collection(  # ✅ key change
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learnrag_docs"
)

# ── query ─────────────────────────────────────────────
user_query = input("Enter your query: ")

search_result = vector_store.similarity_search(query=user_query)

context = "\n\n".join([
    f"Page content: {result.page_content}\n"
    f"Page number: {result.metadata.get('page', 'N/A')}\n"
    f"Source: {result.metadata.get('source', 'N/A')}"
    for result in search_result
])

SYSTEM_PROMPT = f"""You are a helpful assistant for answering questions
based on the available context retrieved from a PDF file.
Only answer based on the context provided.
Navigate the user to the correct page number for more details.

Context:
{context}
"""

# ── generate ──────────────────────────────────────────
response = client.models.generate_content(
    model="gemini-2.5-flash",       # ✅ fresh quota
    contents=user_query,
    config={
        "system_instruction": SYSTEM_PROMPT
    }
)

print("\nResponse:")
print(response.text)