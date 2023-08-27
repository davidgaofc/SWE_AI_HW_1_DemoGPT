import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

def load_document(file_path):
    from langchain.document_loaders import TextLoader
    loader = TextLoader(file_path)
    docs = loader.load()
    return docs

def researchAnalyzer(text):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0
    )
    system_template = """You are an assistant tasked with analyzing a text 
and identifying areas of future research and related research 
directions."""
    system_message_prompt = 
SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please analyze the following text and identify 
areas of future research and related research directions: '{text}'."""
    human_message_prompt = 
HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(text=text)
    return result

st.title("Research Buddy")

uploaded_file = st.file_uploader("Upload Research Paper", type=["pdf", 
"docx", "txt"])
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        file_path = temp_file.name
        st.session_state['file_path'] = file_path

if 'file_path' in st.session_state:
    document = load_document(st.session_state['file_path'])
    text = "".join([doc.page_content for doc in document])
else:
    text = st.text_area("Copy and Paste Text", value="", height=200)

if st.button("Submit"):
    if text:
        research_areas = researchAnalyzer(text)
    else:
        research_areas = ""

    st.markdown("Research Areas: {}".format(research_areas))
