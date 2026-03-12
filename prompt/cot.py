# chain of thought prompting


from dotenv import load_dotenv
from openai import OpenAI
import json
import time


load_dotenv()

client = OpenAI(
    api_key="AIzaSyBpc_aQXCf03ZG2bAQQZA6j9NAxGnJ9vU4",
    # through this we can make our not tp calls to openai api .
    #calls to google apis
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT="""

YOU are expert of ai assistant in resolving  user quries using chain of thought.
you work on start ,plan and  output steps.
youneed to first plan what needs to be done the plan can be multiple  steps
once you think enough plan has been  done ,finally you will give the final answer to user question.
 

rules:
-strictly follow the given Jsosn output format 
- only run one step at a time 
- the sequence of steps is start (where user gives an input),plan
(that can be multiple times and finally output which is going to the displayed to user )

output format:{"steps":start | plan | output,"content":"string"}

examples:
start: hey can you give 2+2*6/10
paln:{"steps":"plan","content":"seems like user is interested in solving a math problem"}
plan:{"steps":"plan","content":"looking at the problem first we need to solve 2*6 then divide the result by 10 and then add 2 to the result"}
"""

# history making ( automated )

msg_history=[

    {"role":"system","content":SYSTEM_PROMPT},
]

user_query = input("➡️->")
msg_history.append({"role":"user","content":user_query})

while True:
    time.sleep(20) # Wait 2 seconds between steps
    response = client.chat.completions.create(

        model="gemini-2.5-flash",
        response_format={"type":"json_object"},
        messages=msg_history

    )

    raw_result=response.choices[0].message.content
    msg_history.append({"role":"assistant","content":raw_result})
    parsed_result=json.loads(raw_result)


    if parsed_result.get("steps")=="start":
        print("🍑",parsed_result.get("content"))
        continue

    if parsed_result.get("steps")=="plan":
        print("✅",parsed_result.get("content"))
        continue
    if parsed_result.get("steps")=="output":
        print("🎉",parsed_result.get("content"))
        break


# response=client.chat.completions.create(

#         model="gemini-2.5-flash",
#         response_format={"type":"json_object"},
#         messages=[
#             {"role":"system","content":SYSTEM_PROMPT},
#              {"role":"user","content":"hii there solve the math problem 2+2*7/8"},
#             {"role": "assistant","content":json.dumps({"steps":"start","content":"hey can you give 2+2*7/8"})}

#         ]

# )

# print(response.choices[0].message.content)
    



    """
    currently it is not working due to no of request problem 
    gemini 5 request per minite and 100 per day so we need to wait for 20 second between each step to get the response from model and then give the next step to model
    so we use timesleep(20) so make it handle 

    
    but still error 
    
    """