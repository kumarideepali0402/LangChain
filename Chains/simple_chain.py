from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = "Give 5 interesting fact about {topic}",
    input_variables=['topic']
)

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
) 

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser() 

chain = prompt | model | parser

result = chain.invoke({'topic' : "Blackhole"})
print(result)



# to visualise
chain.get_graph().print_ascii()


