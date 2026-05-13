from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful {domain} expert'),
    ('human', 'explain the topic {topic}')
])

prompt = chat_template.invoke({'domain': 'cricket', 'topic':'fielding'})
print(prompt)