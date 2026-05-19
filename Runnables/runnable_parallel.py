from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts  import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id ="Qwen/Qwen2.5-7B-Instruct" ,
    task='text-generatuion'
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template ="Write a linkedin post about {text}",
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template ="Write a tweet post about {text}",
    input_variables = ['text']
)

parallel_chain = RunnableParallel({
    'linkedin': RunnableSequence(prompt1, model, parser),
    'tweet': RunnableSequence(prompt2, model, parser)
})


print(parallel_chain.invoke({'text' : 'AI'}))





