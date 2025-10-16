def chat_with_me(question): 
    from langchain_ollama.llms import OllamaLLM
    from langchain_core.prompts import ChatPromptTemplate

    print("CHAT WITH ME CALLED")
    llm = OllamaLLM(model="gemma3:4b")

    template = """Questions : {question}
    Answer : Let's think step by step. 
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm 
    answer = chain.invoke({"question": question})
    return answer 



