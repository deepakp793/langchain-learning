from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are care er guide'),
    ('human', 'Encourage me to become AI enginner')
])

prompt = chat_template.invoke({})

result  = model.invoke(prompt)

print(result.content)