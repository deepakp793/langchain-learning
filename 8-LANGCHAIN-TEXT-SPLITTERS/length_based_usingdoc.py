from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('8-LANGCHAIN-TEXT-SPLITTERS/Brochure_GenAI_DS_Bootcamp.pdf')

docs= loader.lazy_load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[5].page_content)