from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model ='gpt-4');
model = ChatOpenAI(model ='gpt-4',temperature = 0, max_completion_tokens = 10); #high temperature = "more creativity, random" less- deteministic range 0-2 generally

result = model.invoke("What is capital of India?");
print(result);
print(result.content);