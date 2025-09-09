import streamlit as st


if "messages" not in st.session_state:
    st.session_state["messages"]=[]

def refresh_chats(messages):
    for i in messages:
        with st.chat_message(i["role"]):
            st.text(i["content"])

if user_message:=st.chat_input("type here..."):
    st.session_state["messages"].append({"role":"user","content":user_message})
    refresh_chats(st.session_state["messages"])
