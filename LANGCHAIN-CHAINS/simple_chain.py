from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template= 'Give me 5 line motivation to become {career_field} and list of only key skills',
    input_variables=['career_field']
)

parser = StrOutputParser()

chain = prompt | model | parser

result =  chain.invoke({'career_field':'GenAI engineer'})

print(result)

chain.get_graph().print_ascii()