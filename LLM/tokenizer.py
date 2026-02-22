import tiktoken

enc =tiktoken.encoding_for_model("gpt-4o")

text="Hello, how are you doing today? I hope you're having a great day! Let's talk about tokenization and how it works in language models."
tokens=enc.encode(text)

print(tokens)

decodetoken = enc.decode(tokens)
print(decodetoken)
