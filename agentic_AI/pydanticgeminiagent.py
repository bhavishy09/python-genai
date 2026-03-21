import json
import time
import os
import requests
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
from typing import Optional, Literal

# Load environment variables
load_dotenv()

# Setup Client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 1. Define the Pydantic Schema
class MyOutput(BaseModel):
    # Using Literal ensures the model ONLY picks from these 4 strings
    steps: Literal["start", "plan", "tool", "output"] = Field(
        ..., description="The current step in the chain of thought process."
    )
    content: Optional[str] = Field(
        None, description="The reasoning or final answer displayed to the user."
    )
    tool: Optional[str] = Field(
        None, description="Name of the tool to call (if steps is 'tool')."
    )
    input: Optional[str] = Field(
        None, description="The argument/input for the tool call."
    )

def get_weather(city: str):
    url = f"http://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"weather in {city}: {response.text.strip()}"
    return "Sorry, I couldn't fetch the weather information right now."

available_tools = {
    "get_weather": get_weather
}

def run_command(cmd:str):
    result =os.system(cmd)
    return result

SYSTEM_PROMPT = """
YOU are an expert AI assistant resolving user queries using chain of thought.
Sequence: start -> plan -> tool (if needed) -> output.
Available tools: 
- get_weather: takes city name as input.
- run_command: takes a shell command as input and executes it on the server (use with caution).
"""

# 2. Main Logic
msg_history = []

while True:
    user_query = input("\n➡️ -> ")
    if user_query.lower() in ["exit", "quit"]: break
    
    msg_history.append({"role": "user", "parts": [{"text": user_query}]})

    while True:
        try:
            # 3. Use response_schema for strict validation
            response = client.models.generate_content(
                model="gemini-2.5-flash", # Use the stable flash model
                contents=msg_history,
                config={
                    'system_instruction': SYSTEM_PROMPT,
                    'response_mime_type': 'application/json',
                    'response_schema': MyOutput, # This is where the magic happens
                }
            )
        except Exception as e:
            print(f"❌ API Error: {e}")
            break

        # 4. Use the parsed object directly
        # The SDK automatically parses the JSON into your Pydantic model
        res: MyOutput = response.parsed
        
        # Add to history (converting back to dict for the API)
        msg_history.append({"role": "model", "parts": [{"text": json.dumps(res.model_dump())}]})
        
        if res.steps == "start":
            print("🍑", res.content)
        
        elif res.steps == "plan":
            print("✅", res.content)

        elif res.steps == "tool":
            print("🔧", f"calling tool {res.tool} with input {res.input}")
            if res.tool in available_tools:
                result = available_tools[res.tool](res.input)
                msg_history.append({"role": "user", "parts": [{"text": f"Observation: {result}"}]})
            else:
                msg_history.append({"role": "user", "parts": [{"text": f"Error: Tool {res.tool} not found."}]})
        
        elif res.steps == "output":
            print("🎉", res.content)
            break