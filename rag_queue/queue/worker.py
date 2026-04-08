from dotenv import load_dotenv
import os
from pathlib import Path
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from google import genai


load_dotenv(Path(__file__).parent.parent / ".env")
api_key = os.getenv("GOOGLE_API_KEY")
client  = genai.Client(api_key=api_key)


embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=api_key
)

vector_store = QdrantVectorStore.from_existing_collection(  # ✅ key change
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learnrag_docs"
)

def process_query(query):
    print(f"Processing query: {query}")
    search_result = vector_store.similarity_search(query=query)

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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
        config={
            "system_instruction": SYSTEM_PROMPT
        }
    )

    print("\nResponse:")
    print(response.text)
    return response.text



    """
    
    to get result from queue system we have to run function
    process_query in worker.py and we have to run rq worker in terminal to get the result from the queue system
    
    rq worker but in macos

first run export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES in terminal and then run rq worker in terminal to get the result from the queue system

then rq worker --with-scheduler in terminal to get the result from the queue system with scheduler
   
   
   rq worker --with-scheduler run this command in 
   different terminal and request in flask docs to get differnet result 
     """