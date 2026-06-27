from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

loader = TextLoader('LANGCHAIN-DOCUMENT-LOADERS/poem.txt')

doc = loader.load()

prompt = PromptTemplate(
    template= 'write a summary of this poem \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'poem' : doc[0].page_content})

print(result)

print(doc)

print(type(doc))

print(doc[0].page_content)

print(doc[0].metadata)