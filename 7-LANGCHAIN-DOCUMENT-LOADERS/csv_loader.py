from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('7-LANGCHAIN-DOCUMENT-LOADERS/Social_Network_Ads.csv')

docs = loader.load()

print(docs[0])
