import streamlit as st
from backend import ping

if "messages" not in st.session_state:
    st.session_state.messages = []
if user_message:=st.chat_input("type here..."):
    st.session_state["messages"].append({"role": "user", "content": user_message})  
    with st.spinner("wait 🦖🦖🦖..."):
        pong=ping(user_message)['messages'][-1].content
        print(pong)
        st.session_state["messages"].append({"role": "🦖", "content": pong})  

for i in st.session_state["messages"]:
    st.chat_message(i["role"]).markdown(i["content"])
