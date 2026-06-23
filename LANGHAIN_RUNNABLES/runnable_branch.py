from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableBranch

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= 'write a summary of {text}',
    input_variables=['text']
)

report_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x : len(x.split())>300, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

chain = RunnableSequence(report_chain,branch_chain)

result = chain.invoke({'topic':'roadmap to GenAI engineer'})

print(result)