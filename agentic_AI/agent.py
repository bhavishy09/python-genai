# chain of thought prompting
import json
import time
from google import genai
import os
from dotenv import load_dotenv
import requests


# Load environment variables from .env file
load_dotenv()

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

def get_weather(city:str):
    url=f"http://wttr.in/{city.lower()}?format=%C+%t"
    response=requests.get(url)
    if response.status_code==200:
        return f"weather in {city}: {response.text.strip()}"
    else:
        return "Sorry, I couldn't fetch the weather information right now."

# Keep keys matching the prompt's expected tool name
available_tools={
    "get_waether": get_weather
}

SYSTEM_PROMPT="""
YOU are an expert AI assistant resolving user queries using chain of thought.
You work in steps: start, plan, tool, and output.
You need to first plan what needs to be done. The plan can have multiple steps.
Once you have planned enough, finally give the final answer to the user.
 
You can also call tools if required to get the information to answer user question but you need to give one step at a time and follow the output format strictly.
For every tool call, wait for the observation step which is the output of the tool call and then give the next step to the model.

Rules:
- Strictly follow the given JSON output format.
- Only run one step at a time.
- The sequence of steps is: start -> plan -> tool -> output.

Output format: {"steps": "start" | "plan" | "output" | "tool", "content": "string", "tool": "string", "input": "string"}

Available tools: 
- get_waether: takes city name as input and returns weather info about city.
"""

msg_history=[
  
   
]
while True:
 user_query = input("➡️-> ")
 msg_history.append({"role": "user", "parts": [{"text": user_query}]})






 while True:
        # Gemini 2.0 Flash is fast and usually has better rate limits for free tier
        time.sleep(2) 
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=msg_history,
                config={
                    'system_instruction': SYSTEM_PROMPT,
                    'response_mime_type': 'application/json',
                }
            )
        except Exception as e:
            print(f"❌ API Error: {e}")
            break

        if not response.text:
            print("❌ Empty response from model.")
            break

        raw_result = response.text
        # Add model's response to history
        msg_history.append({"role": "model", "parts": [{"text": raw_result}]})
        
        try:
            parsed_result = json.loads(raw_result)
        except json.JSONDecodeError:
            print(f"❌ Error: Model did not return valid JSON. Raw: {raw_result}")
            break

        step = parsed_result.get("steps")

        if step == "start":
            print("🍑", parsed_result.get("content"))
            continue

        if step == "tool":
            tool_name = parsed_result.get("tool")
            tool_input = parsed_result.get("input")
            print("🔧", f"calling tool {tool_name} with input {tool_input}")
            
            if tool_name in available_tools:
                tool_response = available_tools[tool_name](tool_input)
                # Send observation back to the model
                observation = {"steps": "plan", "tool": tool_name, "output": tool_response}
                msg_history.append({"role": "user", "parts": [{"text": f"Observation: {json.dumps(observation)}"}]})
            else:
                msg_history.append({"role": "user", "parts": [{"text": f"Error: Tool {tool_name} not found."}]})
            continue

        if step == "plan":
            print("✅", parsed_result.get("content"))
            continue

        if step == "output":
            print("🎉", parsed_result.get("content"))
            break
