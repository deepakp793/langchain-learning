from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

openAIModel = ChatOpenAI()

gemeniModle = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

tweetprompt = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

linkedinprompt = PromptTemplate(
    template='Generate a linkedin post on {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet' : RunnableSequence(tweetprompt, openAIModel, parser),
    'linkedin': RunnableSequence(linkedinprompt,gemeniModle,parser)
})

result = chain.invoke({'topic':'AI'})

print(result)
