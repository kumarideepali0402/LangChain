from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=32)



documents = [
    "delhi is capital of India",
    "delhi is capital of India",
    "delhi is capital of India"

]
result = embeddings.embed_query(documents);

print(str(result));