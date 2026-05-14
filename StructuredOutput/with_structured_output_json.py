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

json_schema = {
} 


structured_model = model.with_structured_output(json_schema)
result = structured_model.invoke('''I recently bought the Sony WH-1000XM5 headphones and I'm blown away. The noise cancellation is absolutely incredible — I can't hear anything around me. Sound quality is rich and detailed. Battery life easily lasts 30+ hours. They're a bit pricey but totally worth every penny. Highly recommend!
 ''')



print(result)

