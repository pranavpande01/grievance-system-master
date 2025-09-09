import streamlit as st
from uuid import uuid4

if "messages" and "curr_thread_id" not in st.session_state:
    st.session_state["messages"]=[]
    st.session_state["curr_thread_id"]=str(uuid4())


def refresh_chats(messages):
    for i in messages:
        if i["thread_id"]==st.session_state["curr_thread_id"]:
            with st.chat_message(i["role"]):
                st.text(i["content"])

def refresh_sidebar(messages):
    for i in set([message['thread_id'] for message in messages]):
        if st.sidebar.button(i):
            print("okay")

if user_message:=st.chat_input("type here..."):
    st.session_state["messages"].append({"thread_id":st.session_state["curr_thread_id"],"role":"user","content":user_message})
    refresh_chats(st.session_state["messages"])
    refresh_sidebar(st.session_state["messages"])


#st.sidebar.title("hi")
    
if st.sidebar.button("new chat"):
    #send distress signal

    #clear session
    #st.session_state["messages"]=[]
    st.session_state["curr_thread_id"]=str(uuid4())
    refresh_chats(st.session_state["messages"])
    refresh_sidebar(st.session_state["messages"])

    

