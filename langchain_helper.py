from langchain_community.document_loaders import CSVLoader
from langchain.indexes.vectorstore import VectorstoreIndexCreator
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

file_path = "/Users/jiapannan/PycharmProjects/pythonProject/pythonProject/1000 Assistant API/LangChain/test/naver_blog.csv"    
local_persist_path  = "./vector_store"

def get_index_path(index_name):
    return os.path.join(local_persist_path,index_name)

def load_csv_and_save_to_index(file_path,index_name):
    loader = CSVLoader(file_path)
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":get_index_path(index_name)}).from_loaders([loader]) # defult enbedding: OpenAIEmbeddings
    index.vectorstore.persist()

def load_index(index_name):
    index_path = get_index_path(index_name)
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=index_path,embedding_function=embedding)
    return VectorStoreIndexWrapper(vectorstore=vectordb)

def query_index_lc(index, question):
    llm = ChatOpenAI( temperature=0, model_name='gpt-4-turbo-preview')
    ans = index.query(question,llm=llm) 
    return ans


# index = load_index("test2")
# question = "tell me about Ga-ahisas"
# # query_index_lc(index, question)
# print(query_index_lc(index, question))

# index = load_index("test2")
# question ="tell me about Ga-ahisas"
# query_index_lc(index,question)

# load_csv_and_save_to_index(file_path, "test2")


# ans = index.query("tell me about Ga-ahisas")
# print(ans)

# def get_index_path(index_name):
#     return os.path.join(local_persist_path,index_name)

# def load_csv_and_save_to_index(file_path,index_name):
#     loader = CSVLoader(file_path=file_path)
#     index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":local_persist_path}).from_loaders([loader])
#     index.vectorstore.persist()

# def load_index(index_name):
#     index_path = get_index_path(index_name)
#     embedding = OpenAIEmbeddings()
#     vectordb = Chroma(persist_directory=index_path,embedding_function=embedding)
#     return VectorStoreIndexWrapper(vectorstore=vectordb)

# def query_index_lc(index,query):
#     ans = index.query_with_sources(query,chain_type = "map_reduce")
#     return ans["answer"]

# # load_csv_and_save_to_index(file,"travel_blog")

# index = load_index("travel_blog")
#ans = index.query("tell me about Ga-ahisas")
# print(ans)



