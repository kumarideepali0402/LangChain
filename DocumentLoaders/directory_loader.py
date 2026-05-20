#for folder having multiple files/pdf

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'books',
    glob = '*.pdf', #file type
    loader_cls = PyPDFLoader
)

docs1 = loader.load()


# print(docs1[23].page_content)

#limitation -> so many files inside directory takes a lot of time and space in RAM so we have a solution called lazy loaduing

# load() -> eager loading(all files at once)
#lazy_load() -> generator of docs(doc fetched one at a time as needed)

docs2 = loader.lazy_load()

for doc in docs2:
    print(doc.metadata) #loaded one by one as needed

