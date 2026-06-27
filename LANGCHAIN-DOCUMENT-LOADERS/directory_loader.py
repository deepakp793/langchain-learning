from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='LANGCHAIN-DOCUMENT-LOADERS/PDFs',
    glob= '*.pdf',
    loader_cls=PyPDFLoader
    )

docs = loader.load()

print(len(docs))
print(docs[6].page_content)
print(docs[6].metadata)