from langchain_core.tools import tool 

@tool
def add(a: int, b: int): 
    "perform addition by taking two input values and add them"
    return a + b