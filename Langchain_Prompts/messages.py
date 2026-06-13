from langchain_core.messages import SystemMessage, AIMessage,HumanMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a career guide"),
    HumanMessage(content="Will I become AI developer. Give expalanation in minimum word")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)