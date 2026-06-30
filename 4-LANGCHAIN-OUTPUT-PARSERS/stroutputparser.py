from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model

result = chain.invoke({'topic':'Career in AI'})

print(result)