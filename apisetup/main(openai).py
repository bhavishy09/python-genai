"""
code of openai api setup and usage
"""


from dotenv import load_dotenv
from openai import OpenAI

# responsible for loading env file
load_dotenv()

client = OpenAI()

response=client.chat.completions.create(

        model="gpt-4o-mini",
        messages=[
             {"role":"user","content":"hii there"}
        ]



)

print(response.choices[0].message.content)