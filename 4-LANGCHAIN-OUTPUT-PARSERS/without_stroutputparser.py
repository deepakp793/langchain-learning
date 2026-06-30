from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'Qwen/Qwen2.5-7B-Instruct',
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

#prompt1
template1 = PromptTemplate(
    template = """Generate a report on '{topic}'""",
    input_variables=['topic']
)

#prompt2
template2 =  PromptTemplate(
    template="""Generate five line summary of below report. /n '{report}'""",
    input_variables=['report']
)

prompt1 = template1.invoke({'topic':'Career in AI'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'report':result1.content})

resutl2 = model.invoke(prompt2)

print(resutl2)