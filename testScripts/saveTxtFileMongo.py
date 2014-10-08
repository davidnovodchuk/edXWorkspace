f = open('data.txt')  # open a file
text = f.read()    # read the entire contents, should be UTF-8 text

lines = text.split('\n')
names = lines[1].split('|') 

# grid_data is a 2d list that contains all data from the 'data.txt' file
with open('data.txt') as f:
    grid_data = [i.split('|') for i in f.readlines()]

rows = len(grid_data)

result = float(grid_data[100][5]) + float(grid_data[200][3])
print result

"""
# code to read .txt file and save it's name and content in the database

from pymongo import MongoClient

client = MongoClient()
db = client.test_database  # use a database called "test_database"
collection = db.files   # and inside that DB, a collection called "files"

f = open('test_file_name.txt')  # open a file
text = f.read()    # read the entire contents, should be UTF-8 text

# build a document to be inserted
text_file_doc = {"file_name": "test_file_name.txt", "contents" : text }
# insert the contents into the "file" collection
collection.insert(text_file_doc)
"""
