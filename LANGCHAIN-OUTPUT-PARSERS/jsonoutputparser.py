from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2.5-7B-Instruct',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()
print(type(parser))

template = PromptTemplate(
    template= 'Give me Name, City, Age, Height, Weight of {superhero} \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

final_result= chain.invoke({'superhero':'Doctor Strange'})

print(final_result)
print(final_result['Name'])