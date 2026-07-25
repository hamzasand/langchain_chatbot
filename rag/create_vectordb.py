from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

data = PyPDFLoader("C:\\Users\\92324\\Desktop\\cahtbots\\langchain_chatbot\\rag\\deeplearning.pdf")
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)
chunks = splitter(docs)

embedding_model = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents= chunks,
    embeddings = embedding_model,
    persist_directory= "chroma_db"
)