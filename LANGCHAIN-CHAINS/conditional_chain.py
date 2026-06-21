from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description='Give a sentiment of feedback')

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template= 'Classify the sentiment of the following feedback /n {feedback} \n{format_instruction}',
    input_variables=['Feedback'],
    partial_variables= {'format_instruction':pydantic_parser.get_format_instructions()}
)

classifier_chain = prompt1 | model | pydantic_parser

prompt2 = PromptTemplate(
    template= 'Generate appropriate response based on this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Generate appropriate response based on this negative feedback \n {feedback}',
    input_variables=['feedback']
)

str_parser = StrOutputParser()

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | str_parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | str_parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'This is good phone'})

print(result)

chain.get_graph().print_ascii()