import streamlit as st
from uuid import uuid4
from datetime import datetime

if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "curr_thread_id" not in st.session_state:
    st.session_state["curr_thread_id"] = str(uuid4())
if "time_of_generation" not in st.session_state:
    st.session_state["time_of_generation"]=datetime.now()
st.sidebar.title("Threads")
threads = list({msg["thread_id"] for msg in st.session_state["messages"]})
if st.session_state["curr_thread_id"] not in threads:
    threads.append(st.session_state["curr_thread_id"])

selected = st.sidebar.radio("select thread", threads, index=threads.index(st.session_state["curr_thread_id"]))
st.session_state["curr_thread_id"] = selected

if st.sidebar.button("new chat"):
    st.session_state["curr_thread_id"] = str(uuid4())
    st.session_state["time_of_generation"] = datetime.now()

for msg in st.session_state["messages"]:
    if msg["thread_id"] == st.session_state["curr_thread_id"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

if user_input := st.chat_input("Type here..."):
    st.session_state["messages"].append({
        "thread_id": st.session_state["curr_thread_id"],
        "role": "user",
        "content": user_input
    })
    st.rerun()
