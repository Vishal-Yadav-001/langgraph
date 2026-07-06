import streamlit as st
from chatbot_with_memory import chatbot
from langchain_core.messages import BaseMessage,HumanMessage

CONFIG = {"configurable":{"thread_id":"abc"}}

def stream_genrator(user_input):
    stream =  chatbot.stream(
          {"messages":[HumanMessage(content=user_input)]},
          config=CONFIG,
          stream_mode="messages"
     )
    
    for chunk, metadata in stream:
        print(chunk.content)
        if hasattr(chunk, 'content') and chunk.content:
            yield chunk.content

st.title("Agetic Chatbot with Langgraph")

## session state check if present or create new
if "chat_history" not in st.session_state:
     st.session_state.chat_history = [] 

## show existing messsages frpm history
for message in st.session_state.chat_history:
     with st.chat_message(message["role"]):
          st.write(message["content"])




user_input = st.chat_input("Ask llm anything....")

if user_input:
    with st.chat_message('user'):
        st.text(user_input)
    st.session_state.chat_history.append({"role":"user","content":user_input})

    #response = chatbot.invoke({"messages":[HumanMessage(content=user_input)]},config=CONFIG)

   #ai_message = response['messages'][-1].content
    with st.chat_message('assistant'):
        ai_message = st.write_stream(stream_genrator(user_input=user_input))
    st.session_state.chat_history.append({"role":"assistant","content":ai_message})


