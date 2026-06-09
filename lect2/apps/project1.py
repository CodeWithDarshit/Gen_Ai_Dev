from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st 

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
st.title(" ASK ENYTHING - AI QnA Bot")
st.markdown("My QnA Bot With langchain ")

if "messages " not in st.session_state:
    st.session_state.mesaages =[]

    for message in st.session_state.mesaages:
       role = message["role"]
       content = message["content"]
       st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything ? ")

if query:
  st.session_state.mesaages.append({"role":"user", "content": query})
  st.chat_message("user").markdown(query)

  res = llm.invoke(query)
  st.chat_message("ai").markdown(res.content)
  st.session_state.mesaages.append({"role":"ai", "content": res.content})



