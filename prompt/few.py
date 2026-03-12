# few shot prompting: in this we provide some example to model and then ask the question to model . so that model can understand the pattern and then give the answer to our question .
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key="AIzaSyBpc_aQXCf03ZG2bAQQZA6j9NAxGnJ9vU4",
    # through this we can make our not tp calls to openai api .
    #calls to google apis
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

#  few shot promopting: direct give the instruction to model  providing few example to model
SYSTEM_PROMPT= """only answer coding related problems if user ask something other than coding just say sorry .


examples:
Q: how to lean english?
ans: sorry i only help with coding question 


"""
response=client.chat.completions.create(

        model="gemini-2.5-flash",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
             {"role":"user","content":"hii there solve the math problem 2+2"}
        ]



)

print(response.choices[0].message.content)

""" 1.it is using many in real world so you can give at least 50 to 60 examples at least 

2. few shot prompting bind output quality as well .

system_prompt=



 give answer in json format only and answer should contain two keys one is code and other is iscodingquestion

Q. how to lean english?
A: {{"code":null,"iscodingquestion":false}}
"""



