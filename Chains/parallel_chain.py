from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational"
)
model1 = ChatHuggingFace(llm=llm1)

llm2 = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational"
)
model2 = ChatHuggingFace(llm=llm2)

prompt1 = PromptTemplate(
    template="Genarate short simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2  =PromptTemplate(
    template='Generate 5 short question from the following text \n {text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single documnet \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['text', 'quiz']
)


parser = StrOutputParser()

parallel_chain  = RunnableParallel({
    'notes' : prompt1 | model1| parser,
    'quiz' : prompt2| model2 | parser
})
merge_chain = prompt3 | model1 | parser


chain = parallel_chain | merge_chain

text = '''A Support Vector Machine (SVM) is a powerful supervised machine learning algorithm used for classification and regression tasks. It works by finding the optimal "hyperplane" (a boundary line in 2-D or a flat plane in 3-D) that divides data into distinct classes, maximizing the margin between them.'''
chain.invoke({'text' : text})


chain.get_graph().print_ascii()