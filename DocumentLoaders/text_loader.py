from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()

llm = HuggingFaceEndpoint(
    repo_id ="Qwen/Qwen2.5-7B-Instruct" ,
    task = "text-generation"
)

model = ChatHuggingFace(llm= llm)

prompt = PromptTemplate(
    template='write a summary of {poem}',
    input_variables=['poem']
)


loader = TextLoader('chat_history.txt', encoding='utf-8')

docs = loader.load()

print(type(docs)); #list
print(len(docs)); #1

print((type(docs[0]))); #document

print(docs[0].metadata);

print(docs[0].page_content)

chain = prompt | model | parser

result= chain.invoke({'poem' : docs[0].page_content})

print(result)




