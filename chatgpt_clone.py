import openai
import gradio as gr
from dotenv import  load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = "Insert API Key"

def myGPT(message,history):
    messages = []
    messages.append({"role":"user","content": message})
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = messages,
        max_tokens=150,
        top_p=1,
        temperature = 0.9,
        frequency_penalty=0,
        presence_penalty=0.6
    )

    output = response['choices'][0]['message']['content']
    return output

gr.ChatInterface(myGPT).launch()