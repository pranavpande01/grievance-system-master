import streamlit as st
from backend import ping

if user_message:=st.chat_input("type here..."):
    with st.spinner("bitch"):
        pong=ping(user_message)['messages'][-1].content
        st.markdown(pong)
        print(pong)
    