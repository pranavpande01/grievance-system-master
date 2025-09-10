import streamlit as st
from backend import ping

if user_message:=st.chat_input("type here..."):
    with st.spinner("bitch"):
        st.markdown(ping(user_message)['messages'][-1].content)
    