from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
) 

model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name: str = Field("Name of person")
    age:int = Field("Age of the person")
    city:str = Field("City where person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables={'place'},
    optional_variables={'format_instruction': parser.get_format_instructions()}
   
)
# prompt = template.invoke({'place' : 'Indian'})

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# print(final_result)

chain = template | model | parser

final_result = chain.invoke({'place': 'Sri Lankan'})

print(final_result)