from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage,HumanMessage
from typing import TypedDict, Annotated
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
from langgraph.checkpoint.memory import MemorySaver
os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")
## Initialise LLM
llm = ChatGroq(model="openai/gpt-oss-120b")

thread = "abcd"
config = {"configurable":{"thread_id":thread}}


## Define State
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
### Define Node Chat Node

def chat_with_llm(state:State):
    ## take user messages from state
    messages = state['messages']

    ## call llm by passing messages / message history
    response = llm.invoke(messages)
    #print("Response",response,end="??????")

    return {"messages":[response]}

## Define memory saver checkpoint
checkpoint = MemorySaver()
## Define graph
graph = StateGraph(State)
## add nodes
graph.add_node("chat_with_llm",chat_with_llm)

## add edges
graph.add_edge(START,"chat_with_llm")
graph.add_edge("chat_with_llm",END)

## compile graph
chatbot = graph.compile(checkpointer=checkpoint)
