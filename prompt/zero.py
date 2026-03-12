# zero shot prompting
"""


"""

# these calls are done by google llm 
# using openai library to make calls to google llm api

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key="AIzaSyBpc_aQXCf03ZG2bAQQZA6j9NAxGnJ9vU4",
    # through this we can make our not tp calls to openai api .
    #calls to google apis
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

#  zero shot promopting: direct give the instruction to model without providing any example to model
SYSTEM_PROMPT= "only answer coding related problems if user ask something other than coding just say sorry ."
response=client.chat.completions.create(

        model="gemini-2.5-flash",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
             {"role":"user","content":"hii there solve the math problem 2+2"}
        ]



)

print(response.choices[0].message.content)