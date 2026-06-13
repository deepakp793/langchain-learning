from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    user_sentiment : str
    rating : int

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The Monitor is great for gaming but its not giving good color while video ediing. For gaming its high refresh rate giving faboulus experience. But also I am working on some video editing I see poor performance of this monitor there. I would not recommend this for video editing but great for gaming. I would give 5 star rating for this""")

print(result)
print(result['user_sentiment'])
print(result['rating'])

