from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are career guide. Answer me each question in minimum words')    
]

while True:
    user_input = input('You: ')
    if user_input == 'exit':
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history).content
    chat_history.append(AIMessage(content=result))
    print("AI: ",result)

print(chat_history)
