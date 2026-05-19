from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()

llm = HuggingFaceEndpoint(
    repo_id ="Qwen/Qwen2.5-7B-Instruct" ,
    task = "text-generation"
)

model = ChatHuggingFace(llm= llm)



prompt1 = PromptTemplate(
    template="Write about {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template="Write a summary of {topic}",
    input_variables = ['topic']
)

chain1 = RunnableSequence(prompt1, model, parser);


branch_chain = RunnableBranch(
    (lambda x: len(x.split()) < 300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain =  RunnableSequence(chain1, branch_chain)
result = final_chain.invoke({'topic': "ai"})
print(result)