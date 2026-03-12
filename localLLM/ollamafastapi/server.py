from fastapi import FastAPI, Body
from ollama import Client
app = FastAPI()

Client =Client(
    host="http://localhost:11434",
)
@app.post("/chat")

def chat(
        
     message: str=Body(..., description="The message "),

) :
   response = Client.chat(model="gemma:2b", messages=[{"role": "user", "content": message}])
   return {"response": response.message.content}