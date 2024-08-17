import streamlit as st
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredFileLoader
from langchain import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
# from google.colab import userdata # Not needed on Streamlit Cloud
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from IPython.display import display
from IPython.display import Markdown
import textwrap

# Get API key from environment variable (preferred) or secrets file
# GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
# or
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)

# Setup the directory where files are stored
pdf_directory = "./board_games" # Adjust if your PDFs are in a different subdirectory

# LLM and LangChain code
#------------------------------------------------------

# Create a list to store the PDFs
documents = []

# Iterate through each file in the directory
# for filename in os.listdir(pdf_directory):
#     if filename.endswith(".pdf"):
#         filepath = os.path.join(pdf_directory, filename)
#         loader = PyPDFLoader(filepath)
#         documents.extend(loader.load())

for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        filepath = os.path.join(pdf_directory, filename)

        # Prompt the user for the password if the PDF is encrypted
        try:
            loader = PyPDFLoader(filepath)
            documents.extend(loader.load())
        except PyPDFLoader.EncryptedFileError:
            password = st.text_input(f"Enter password for {filename}:", type="password")
            if password:
                loader = PyPDFLoader(filepath, password=password)
                documents.extend(loader.load())
            else:
                st.warning(f"Skipping {filename} due to missing password.")


# Split the documents into smaller chunks for efficient processing
text_splitter = RecursiveCharacterTextSplitter(chunk_size=6000, chunk_overlap=750)
docs = text_splitter.split_documents(documents)

# Create a Chroma vectorstore for efficient document retrieval
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
vectordb = Chroma.from_documents(docs, embeddings)

# Initialize the Google Gemini 1.5 Flash model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY, temperature=0.2)

# Get user input and generate a response
template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just mention that you we do not support this currently and do no try to make up an answer and mention that we may support it in the future. Always say "Thanks for asking" at the end of the answer.
{context}
Question: {question}
Answer:"""

QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
qa_chain = RetrievalQA.from_chain_type(
    model,
    retriever=vectordb.as_retriever(search_kwargs={"k": 5}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

# -----------------------------------------------------

# Streamlit app
st.title("Board Game FAQ Chat App")

# Get user input
query = st.text_input("Ask a question about the board games:")

# Display response if a query is provided
if query:
    with st.spinner("Searching through the rulebooks..."):
        result = qa_chain({"query": query})
        st.markdown(result["result"])
