from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='LANGCHAIN-DOCUMENT-LOADERS/PDFs',
    glob= '*.pdf',
    loader_cls=PyPDFLoader
    )

#load function load all the documents at a time in memory
docs1 = loader.load()

#lazy_load function fetch a document and load in memory on demand basis
docs2 = loader.lazy_load()

for document in docs1:
    print(document.metadata)

for document in docs2:
    print(document.metadata)