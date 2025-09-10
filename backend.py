from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from typing import TypedDict,List,Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.prebuilt import ToolNode, tools_condition
import json
from tools import calculator,search_tool,date, console,delay,send_email

load_dotenv()

toolbox=[calculator,search_tool,date,console,delay,send_email]
#################################################################
# util section
class State(TypedDict):
    messages:Annotated[List[BaseMessage],add_messages]

def invoke_llm(msessages:State):
    llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    llm=llm.bind_tools(toolbox)
    message=llm.invoke(msessages['messages'])
    
    return {
        'messages':message
    }


with open('config.json','r') as file: config=json.load(file)
#################################################################

# define checkpoint
checkpoint=InMemorySaver()
# define graph
graph=StateGraph(State)
# define nodes
graph.add_node("invoke_llm",invoke_llm)
graph.add_node("tools",ToolNode(toolbox))
# define edges
graph.add_edge(START,"invoke_llm")
graph.add_conditional_edges("invoke_llm",tools_condition)
graph.add_edge("tools","invoke_llm")
#graph.add_edge("invoke_llm",END)
# compile graph
graph=graph.compile(checkpointer=checkpoint)

#################################################################
# inference
def ping(message):
    global graph
    pong = graph.invoke(
        {'messages': [HumanMessage(content=message)]},
        config=config
    )
    return pong
