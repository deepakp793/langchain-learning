from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

model = ChatOpenAI()

chat_history= [
    SystemMessage(content='Act as a careerguide for me')
]

st.header('AI Guide tool')

template = load_prompt('aitemplate.json')

while True:
    chat_input = input('You :')
    if chat_input == 'exit':
        break
    chat_history.append(HumanMessage(content=chat_input)) 
    chain = template | model
    result = chain.invoke({
        'chat_input' : chat_input,
        'chat_history': chat_history
    })
    print('Response :',result.content)
    chat_history.append(AIMessage(content=result.content))

print(chat_history)

