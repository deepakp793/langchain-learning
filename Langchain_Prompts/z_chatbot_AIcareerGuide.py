from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_core.load import loads

load_dotenv()

model = ChatOpenAI()


with open('Langchain_Prompts/z_aitemplate.json','r') as f:
    saved_prompt_json = f.read()

chat_template = loads(saved_prompt_json)

refer_old_chat = input("AIMessage:You want to use old chat history?")

if refer_old_chat == 'no':
    with open('Langchain_Prompts/z_chat_history.txt', 'w') as f:
        pass



while True:
    chat_history = []
    with open('Langchain_Prompts/z_chat_history.txt') as f:
        chat_history.extend(f.readlines())

    chat_input = input('You :')
    with open('Langchain_Prompts/z_chat_history.txt','a') as f:
        f.write(f"\n{chat_input}")
    if chat_input == 'exit':
        break   
    prompt = chat_template.invoke({
        'chat_history':chat_history,
        'query':chat_input
    })

    result = model.invoke(prompt)
    with open('Langchain_Prompts/z_chat_history.txt','a') as f:
        f.write(f"\n{result.content}")
    print(result.content)

print(chat_history)
