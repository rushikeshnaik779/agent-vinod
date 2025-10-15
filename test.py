from gome import gome
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent

# Use ChatOllama, not OllamaLLM, as only chat models have .bind_tools()
llm = ChatOllama(model="llama3.1", temperature=0)

# The list of tools the agent can use
tools = [gome.add]

# Bind the tools to the chat model
llm_with_tools = llm.bind_tools(tools)

# Define the chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant that can answer questions using tools."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

# Create the agent using the correct LLM and tool binding
agent = create_tool_calling_agent(llm_with_tools, tools, prompt)

# Initialize AgentExecutor with keyword arguments
# This is the fix for the TypeError
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


def agent_worker(query): 
    # Invoke the agent with a query that requires a tool call
    result = agent_executor.invoke(
        {"input": query}
    )

    return result

