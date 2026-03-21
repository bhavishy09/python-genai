from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def main():
    user_input = input("Enter your question: ")
    # 1. Assign response to a variable
    # 2. Complete the syntax with ")" and remove the "\"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    # 3. Use the correct OpenAI response structure
    # 4. Move print inside the function scope where response is defined
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
