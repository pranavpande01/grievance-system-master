from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from typing import TypedDict,List,Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
load_dotenv()

#################################################################
# util section
class State(TypedDict):
    messages:Annotated[List[BaseMessage],add_messages]

def invoke_llm(msessages:State):
    llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")
    return llm.invoke(msessages['messages'])



#################################################################

# define checkpoint
checkpoint=InMemorySaver()
# define graph
graph=StateGraph(State)
# define nodes
graph.add_node("invoke_llm",invoke_llm)
# define edges
graph.add_edge(START,"invoke_llm")
graph.add_edge("invoke_llm",END)
# compile graph
graph=graph.compile(checkpointer=checkpoint)

#################################################################
# inference
a=graph.invoke("hi what a lovely day")
print(a)
