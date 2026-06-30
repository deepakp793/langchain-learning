from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic("claude-sonnet-4-6")

result = model.invoke("What is the giant organisation in AI implemetation")

print(result.content)