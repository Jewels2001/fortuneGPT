import os
import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('API_KEY')

chatCompletion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                    messages=[{"role": "system",
                               "content": "You are a free-spirited fortune teller giving advice, scholarly quotes, and jokes. Do not state what you are doing. Keep it short."},
                              {"role": "user",
                               "content": "What is my fortune?"}])

print(chatCompletion.choices[0].message.content)