from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
answer the question below.
here is the question history: {context}
question: {question}
answer:
"""

model = OllamaLLM(model="llama3")
promt = ChatPromptTemplate.from_template(template)
chain = promt | model

def handle_conversation():
    context = ""

    # Primera pregunta automatizada (no mostrada al usuario)
    initial_question = "Please rolplay as Barack Obama in this conversation"
    result = chain.invoke({"context": context, "question": initial_question})
    context += f"\nAI: {result}"

    print("Welcome to the Obama chatbot, type 'exit' to quit.")
    
    # Loop para manejar el resto de la conversación
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        # Añadir una línea en blanco entre "You:" y "Obama:"
        print(f"\nObama: {result}")  
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()



# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import ChatPromptTemplate
# template = """
# answer the question below.
# here us the question history: {context}
# question: {question}
# answer:
# """

# model = OllamaLLM(model="llama3")
# promt = ChatPromptTemplate.from_template(template)
# chain = promt | model

# def handle_conversation():
#     context= ""
#     print("welcome to the ollama chatbot, type 'exit' to quit.")
#     while True:
#         user_input = input("you: ")
#         if user_input.lower() == "exit":
#             break
#         result = chain.invoke({"context": context, "question": user_input})
#         print("ollama: ", result)
#         context += f"\nUser: {user_input}\nAI:{result}"
# if __name__ == "__main__":
#     handle_conversation()