#extract text content from webpages(urls)

# internally it uses BeautifulSoup(to understand html structure) and request(to make http request)



from langchain_community.document_loaders import WebBasedLoader

url = 'https://www.coursera.org/learn/dao-3022/supplement/XN5tW/ppt-week-3'
# we can pass list of urls as well

loader  = WebBasedLoader(url)

docs = loader.load()

print(len(docs));

print(docs[0].page_content)
