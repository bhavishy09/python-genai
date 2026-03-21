from google import genai
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


def get_waether(city:str):
    url=f"http://wttr.in/{city.lower()}?format=%C+%t"
    response=requests.get(url)
    if response.status_code==200:
        return f" weather{city} {response.text.strip()}"
    else:
        return "Sorry, I couldn't fetch the weather information right now."




def main():
    user_input = input("Enter your question: ")
    
    # Corrected usage for the google-genai SDK.
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=user_input
    )
    print(response.text)
    
print(get_waether("goa"))

if __name__ == "__main__":
    main()
