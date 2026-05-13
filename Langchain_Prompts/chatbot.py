from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage


load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2.5-7B-Instruct',
    task='text-generation',
)

model = ChatHuggingFace(llm=llm);


# chat_history = []
chat_history = [
    SystemMessage(content='you are a helpful ai assistant')
]


while True :
    user_input = input("You: ");
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)