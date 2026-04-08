#fast api code 
from dotenv import load_dotenv
import os
from pathlib import Path
from fastapi import FastAPI , Query
from .client.rq_client import queue
from .queue.worker import process_query
app = FastAPI()

load_dotenv(Path(__file__).parent / ".env")

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/chat")
def chat(
    query: str = Query(..., description="The query to process")
):
   job= queue.enqueue(process_query, query)
   return {"status": "Query enqueued", "job_id": job.id}

@app.get("/result")
def get_result(
      job_id: str = Query(..., description="The ID of the job to retrieve the result for")        
):
   job = queue.fetch_job(job_id=job_id)
   result = job.return_value()
   return { "result": result}
  
