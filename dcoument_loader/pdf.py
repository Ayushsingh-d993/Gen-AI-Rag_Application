from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("ayush.pdf")

docs = data.load()
print(docs)