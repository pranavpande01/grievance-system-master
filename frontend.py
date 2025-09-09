import streamlit as st
from uuid import uuid4

if "messages" and "sessions" not in st.session_state:
    st.session_state["messages"]=[]


def refresh_chats(messages):
    for i in messages:
        with st.chat_message(i["role"]):
            st.text(i["content"])
def refresh_sidebar(messages):
    for i in messages:
        st.button(i["thread_id"])

if user_message:=st.chat_input("type here..."):
    st.session_state["messages"].append({"thread_id":1,"role":"user","content":user_message})
    refresh_chats(st.session_state["messages"])


#st.sidebar.title("hi")
    
if st.sidebar.button("new chat"):
    #send distress signal
    #clear session
    st.session_state["messages"]=[]
    refresh_chats(st.session_state["messages"])

    

