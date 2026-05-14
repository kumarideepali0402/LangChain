from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import TypedDict,Annotated, Optional, Literal
from dotenv import load_dotenv

load_dotenv();

llm = HuggingFaceEndpoint(
   repo_id='Qwen/Qwen2.5-7B-Instruct',
    task = 'text-generation'
)

model = ChatHuggingFace(llm = llm);

# class Review(TypedDict):
#     summary: str
#     sentiment: str

class Review(TypedDict):
    key_themes: Annotated[list[str], "give key themes in the form of list"]
    summary: Annotated[str,"brief summary of review"]
    sentiment: Annotated[Literal["pos", "neg"],"Sentiment of reviewr"]
    pros: Annotated[Optional[list[str]],"pros of review"]


structured_model = model.with_structured_output(Review)
result = structured_model.invoke('''I recently bought the Sony WH-1000XM5 headphones and I'm blown away. The noise cancellation is absolutely incredible — I can't hear anything around me. Sound quality is rich and detailed. Battery life easily lasts 30+ hours. They're a bit pricey but totally worth every penny. Highly recommend!
 ''')



print(result)
print(result["summary"])
print(result["sentiment"])
