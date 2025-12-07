import os
from mistralai import Mistral
#import tiktoken
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("API_KEY"))
MODEL="mistral-small-latest"
TEMPERATURE= 0.7
MAX_TOKENS = 100
SYSTEM_PROMPT = "You are an elegant and calm assistant who loves answering questions"
messages= [{"role": "system", "content": SYSTEM_PROMPT}]


def chatbot(user_input):
    
    messages.append({"role": "user", "content": user_input})
    response = client.chat.complete(
        model= MODEL,
        messages=messages,
     temperature= TEMPERATURE, #temperature is like a scale for AI's creativity for the response
     max_tokens= MAX_TOKENS
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply}) 
    return reply

while True:
    user_input= input("You:")
    if user_input.strip().lower() in {"exit","quit"}:
        break
    answer = chatbot(user_input)
    
    print("Assitant:",answer)
    

