from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template= 'Answer the following question \n {question} based on this information {information}',
    input_variables=['question','information']
)

parser = StrOutputParser()

loader = WebBaseLoader('https://www.amazon.in/dp/B0H3PV7418?_encoding=UTF8&ref_=cct_cg_Header_2a1&pf_rd_p=94d02b33-7d89-4d4a-94f4-ec4082b1e46e&pf_rd_r=4J2H0X4Q8MDQ9Q5CJ5EV&th=1')

docs = loader.load()

chain = prompt | model | parser

question = 'What is the price of this product'

result = chain.invoke({'question':question,'information':docs[0].page_content})

print(result)