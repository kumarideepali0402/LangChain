from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv



load_dotenv()


prompt1 = PromptTemplate(
    template="Write a joke about{topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Explain the joke -{text}",
    input_variables=[{'text'}]
)


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task= 'text-genreration'
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()


chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser);

print(chain.invoke({'topic' : "AI"}))
