
# these calls are done by google llm 
# using openai library to make calls to google llm api

from dotenv import load_dotenv
from openai import OpenAI



load_dotenv()

client = OpenAI(
    api_key="AIzaSyAMrqoNVUcbb7dVXKF8GPqot5iyRbVvZSg",
    # through this we can make our not tp calls to openai api .
    #calls to google apis
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response=client.chat.completions.create(

        model="gemini-2.5-flash",
        messages=[

            # system prompt is first msg special instructions to chatbot
{"role":"system","content":"you are a helpful assistant that helps users solve math problems."},
             {"role":"user","content":"hii there"}
        ]



)

print(response.choices[0].message.content)