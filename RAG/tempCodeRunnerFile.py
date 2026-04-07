from dotenv import load_dotenv
import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
pad_path = Path(__file__).parent / "node.pdf"
from langchain_text_splitters import RecursiveCharacterTextSplitter

#from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings 

from langchain_qdrant import QdrantVectorStore

load_dotenv(Path(__file__).parent / ".env")
api_key = os.getenv("GOOGLE_API_KEY")
# step 1: load the pdf file and convert it into a list of documents
# load this file in python program
loader= PyPDFLoader(file_path=pad_path)
docs = loader.load()

#print(docs[0].page_content)
#step 2: chunking the document into smaller pieces
# by using langchain not manually
#pip install -U langchain-text-splitters

# split the docs into smaller pieces
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
chunks=text_splitter.split_documents(documents=docs)

#step 3: vector  embedding of the chunks ( you can do manually but 
# langchain provides interface for that as well )

# vector embeddings 
#pip install -qU langchain-openai

#embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# store vector embedding in vector database( qdrantdb )
#pip install -qU langchain-qdrant
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learnrag_docs"
    )
 
print("vector store created successfully")