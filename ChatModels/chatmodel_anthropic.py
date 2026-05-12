from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv;


load_dotenv();

model = ChatAnthropic(model = 'claude-opus-4-7');

result = model.invoke("What is Capital of India");
print(result.content);