# used to load content from PDF files and convert each pages into a document object

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Goldman Sachs Aptitude Prep Kit.pdf')

docs = loader.load()

print(docs);
print(len(docs));
print(docs[0].page_content);
print(docs[1].metadata);

#limitation:
#pypdfloader for textual pdf

