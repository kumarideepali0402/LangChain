from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

parser = StrOutputParser()

llm = HuggingFaceEndpoint(
    repo_id ="Qwen/Qwen2.5-7B-Instruct" ,
    task = "text-generation"
)

model = ChatHuggingFace(llm= llm)

prompt1 = PromptTemplate(
    template="Make a joke for the {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template="explain the joke {topic}",
    input_variables = ['topic']
)
joke_gen = RunnableSequence(prompt1, model, parser);

print_explain  = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explain' : RunnableSequence(prompt2, model, parser)

})

final_chain = RunnableSequence(joke_gen,print_explain);

result = final_chain.invoke({'topic' :"AI"})

print(result)