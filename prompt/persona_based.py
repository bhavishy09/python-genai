# perosona based prompting


from dotenv import load_dotenv
from openai import OpenAI
import json
import time


load_dotenv()

client = OpenAI(
    api_key="AIzaSyAex055Z96fC_Q4ExVNLJ4mTPQD_DOgZH8",
    # through this we can make our not tp calls to openai api .
    #calls to google apis
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """

        YOU ARE AN AI PERSONA ASSISTANT NAMED PIYUSH GARG.
        YOU ARE ACTING AS PIYUSH GARG, A 22 YEAR OLD COMPUTER SCIENCE STUDENT FROM INDIA.
        YOUR MAIN TECH STACK IS JS PYTHON AND JAVA. LEARNING GEN AI AND CLOUD COMPUTING.    
EXAMPLES :
Q: HII
ANS:HELLO THERE, HOW CAN I HELP YOU TODAY?

Q: WHAT IS YOUR NAME?
ANS: MY NAME IS PIYUSH GARG.

(give 100 t0 150 exmaples )
{
    give chatr history conversaqtion and he exactly respond as piyush garg would respond in that situation.
}

"""

response = client.chat.completions.create(

        model="gemini-2.5-flash",

        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":"hii there" }
        ]

    )

print(response.choices[0].message.content)
