from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

embeddings = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=32)



documents = [
    "Sachin Tendulkar — Known as the 'God of Cricket,' Sachin scored 100 international centuries and holds the record for the most runs in both Test and ODI cricket.",
    "Kohli -One of the greatest modern-day batters, Kohli has consistently ranked among the top ODI and Test run-scorers and is renowned for his fitness and aggressive playing style.",
    "MS Dhoni -The legendary captain who led India to victories in the 2007 T20 World Cup, 2011 ODI World Cup, and 2013 Champions Trophy, known for his calm temperament and lightning-fast stumpings."

]


query = "telll me about virat kohli"

doc_embeddings = embeddings.embed_documents(documents);
query_embedding = embeddings.embed_query(query);

scores = cosine_similarity([query_embedding],doc_embeddings)[0]
index, score = sorted(list(enumerate(scores), key=lambda x:x[1])[-1])

print(documents[index]);
print("Similarity score is ", score)