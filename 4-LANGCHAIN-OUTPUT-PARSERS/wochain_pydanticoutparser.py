from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= 'Qwen/Qwen2.5-7B-Instruct',
    task= 'text-generation'
)

model = ChatHuggingFace(llm=llm)

class Superhero(BaseModel):
    name : str = Field(description='Name of a superhero')
    age : int = Field(gt=5, description='Age of superhero')
    city : str = Field(description='City of a superhero')

parser =  PydanticOutputParser(pydantic_object= Superhero)

template = PromptTemplate(
    template= 'Provide an information of one superhero from {country} \n {format_instruction}',
    input_variables=['country'],
    partial_variables= {'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({'country':'Indian'})

print(prompt)

result = model.invoke(prompt)

print(result)