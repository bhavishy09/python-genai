from google import genai

client =genai.Client(
    api_key="AIzaSyAMrqoNVUcbb7dVXKF8GPqot5iyRbVvZSg"
)

response= client.models.generate_content(
    model="gemini-2.5-flash", contents="explain how ai work in few words"
   
)

print(response.text)