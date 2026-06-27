from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('LANGCHAIN-DOCUMENT-LOADERS/Brochure_GenAI_DS_Bootcamp.pdf')

docs = loader.load()

print(len(docs))

print(docs[2].page_content)

