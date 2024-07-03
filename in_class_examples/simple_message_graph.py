from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import END, MessageGraph

model = ChatOpenAI(temperature=0)

# First, we initialize our model and a MessageGraph.
graph = MessageGraph()

# Next, we add a single node to the graph, 
# called "oracle", which simply calls the model with the given input.
graph.add_node("oracle", model)

# We add an edge from this "oracle" node to the special string END ("__end__"). 
# This means that execution will end after the current node.
graph.add_edge("oracle", END)

# We set "oracle" as the entrypoint to the graph.
graph.set_entry_point("oracle")

# We compile the graph
runnable = graph.compile()

# How state moves through the graph: 
# 1. LangGraph adds the input message to the internal state.
# 2. Then passes the state to the entrypoint node, "oracle".
# 3. The "oracle" node executes, invoking the chat model.
# 4. The chat model returns an AIMessage. LangGraph adds this to the state.
# 5. Execution progresses to the special END value and outputs the final state.
print(runnable.invoke(HumanMessage("What is 1 + 1?")))

