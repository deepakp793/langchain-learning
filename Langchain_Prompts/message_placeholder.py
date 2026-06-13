from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()


chat_template = ChatPromptTemplate.from_messages([
    ('system','You are a csr assitant. Answer to the query of customer. Refer old chat history'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

with open('chat_history.txt') as f :
    chat_history.extend(f.readlines())

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'where is my refund of order #123'})

result = model.invoke(prompt)

print(result.content)