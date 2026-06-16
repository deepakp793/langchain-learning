from typing import Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

# schema
class Review(BaseModel):
    key_theme: list[str] = Field(description="All the key theme of product")
    summary: str = Field(description="A brief summary of review")
    rating: int = Field(
        description="Overall rating of product based on review.Rate product between 1 to 10"
    )
    pros: Optional[list[str]] = Field(
        default=None, description="Write the pros inside list if abailable"
    )
    cons: Optional[list[str]] = Field(
        default=None, description="Write the cons inside list if abailable"
    )
    name: Optional[str] = Field(
        default=None,
        description="Set the name only if reveiwer real human name explicitly available.",
    )


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """This is first amkette product purchase and I am fully satisfied with the product . I am using the keyboard for around 10 days


Design and Build (4/5) : Good color option and steady plastic build


Battery (5/5) : Great battery life . I Recharged the keyboard to 90% just after delivered and still 50%+ battery left after 10 days on average use of 6hrs/day on 2 devices


Keys (4/5) : Smooth and responsive keys suitable for every day use


Connectivity (3.5/5) : The connectivity is good but experienced Bluetooth connection issue once which is rare and mangeble in every day use.The device switching is seamless as well


Weight and Size (4/5) : Lightweight and compact suitable for travelling .

The compact size may be an issue for people who are frequently using full size keyboard initially they can prefer the full size one . The issue is not with the device it's all about the choice
Review by Andy                                 
"""
)

print(result)
result_dict = result.model_dump()
print(result_dict["key_theme"])
