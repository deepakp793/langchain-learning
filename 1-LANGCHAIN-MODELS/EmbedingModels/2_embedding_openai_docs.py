from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=32)

document = [
    "Delhi is capital of india",
    "Mumbai is capital of Maharashtra"
]

result = embedding.embed_documents(document)

print(str(result))