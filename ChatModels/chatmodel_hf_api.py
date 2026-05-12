from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv(override=True)

token = os.getenv('HUGGINGFACEHUB_ACCESS_TOKEN')
os.environ['HF_TOKEN'] = token  # newer huggingface_hub requires this env var

llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2.5-7B-Instruct',
    task='text-generation',
    huggingfacehub_api_token=token
);

model = ChatHuggingFace(llm = llm);

result = model.invoke("What is the capital of Delhi?");

print(result.content);