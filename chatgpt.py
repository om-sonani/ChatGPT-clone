import openai
import os

# Set your API key
openai.api_key = "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"

# Generate some text
prompt = input("enter your question : ")

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)
message = response.choices[0].text.strip()
print(message) 

