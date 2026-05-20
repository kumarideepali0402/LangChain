# to load csv file 
#it makes document object for each row

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='CSV_file.csv')

data = loader.load()

print(len(data)) #no. of rows
 
print(data[0]) #first row