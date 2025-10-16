# from langchain_ollama.llms import OllamaLLM
# from langchain_core.prompts import ChatPromptTemplate 

# from gome import gome

# print(gome.add(1, 2))

# llm = OllamaLLM(model="gemma3:4b")

# template = """Questions : {question}

# Answer: Let's think steps by step. 
# """

# prompt = ChatPromptTemplate.from_template(template)
# chain = prompt | llm 
# answer = chain.invoke({"question": "Can you explain me few reasons of " \
# "Epam system"})
# print(answer)


from gome import inbuilt_chatinterface

print(inbuilt_chatinterface.chat_with_me("Hey"))