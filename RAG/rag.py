"""
rag is a library for building retrieval-augmented generation (RAG)
 systems. It provides tools for integrating retrieval mechanisms 
 with generative models, allowing for more accurate
and contextually relevant responses. The library includes 
components for indexing and retrieving information from various
 sources, as well as interfaces for connecting to popular 
  generative models.

  
  problem is 
  -->LLM DOEST NOT KNOW EVERYTHING, ABOUT YOUR PRIVATE DATA.
  -->context window is limited, so you can only give it 
limited information.


these above are some problems that RAG is trying to solve 
by giving the LLM access to external data sources
 and retrieval mechanisms.


 example -> you have bunch of files and you want to convert into 
 text and prepare the system prompt (have all the available information in the system prompt) 
 .-> then building a chatbot on top of that system prompt 
 and then you can ask question to the chatbot and 
 it will give you answer based on the information available 
 in the system prompt.

 this is naive approach and it has some problems
 problems
 1.cost
 2.context window  limited (1m token window ()).
 this is also a rag with naive approach but it is not efficient
 and it is not scalable.


 make it more scalabe EXAMPLE -> 50,000 FILES 
 RAG
 1 . Indexing (provide data)-> convert all the files into vector
 and store it in vector database (we will talk about vector database later)

 2. reterival phase -> chatting with data 

 ex->in indexing phase 
files-> chunking -> embedding(model create vector embbedings) -> vector database(store actual
 content and vector embedding)

ex -> in retrieval phase

user query -> embedding -> vector database (find similar content) -> 
give it to the model -> model give answer based on retrieved content
(you get only relevant content to the query and not the whole data)->
gpt5 (we give query and relevant context   )-> user get answer based on the retrieved
 content and not based on the whole data
 

you get relevant answer based on the retrieved content and not based on the whole data

example gpt-5( we give query and relevant context   )


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



chat.py and ragpiple.py are syn ( not production level)

asyn -> lets do this in backgrround and let user do what ever he wants 


queue in system design->(fifo)

   query
     |
     |
     \/
http server ( fast api)


"""