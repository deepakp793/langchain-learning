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
    template= 'Give me Name, City, Age, Height, Weight of Iron Man \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.format()

result = model.invoke(prompt)

print(result)

final_result = parser.parse(result.content)

print(final_result)
print(final_result['Name'])