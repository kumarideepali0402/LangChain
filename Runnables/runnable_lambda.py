from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()

llm = HuggingFaceEndpoint(
    repo_id ="Qwen/Qwen2.5-7B-Instruct" ,
    task = "text-generation"
)

model = ChatHuggingFace(llm= llm)

def countWords(text) :
    return len(text.split())

prompt1 = PromptTemplate(
    template="Make a joke for the {topic}",
    input_variables = ['topic']
)

joke_gen = RunnableSequence(prompt1, model, parser)


# print_count = RunnableParallel({
#     'length': RunnableLambda(countWords),
#     'joke' :RunnablePassthrough()

# })

print_count = RunnableParallel({
    'length': RunnableLambda(lambda x: len(x.split())),
    'joke' :RunnablePassthrough()

})

final_chain = RunnableSequence(joke_gen, print_count)

result = final_chain.invoke({'topic': "AI"});

final_result = ''' {}\n word count - {} '''.format( result["joke"],result["length"])

print(final_result)

