import pymongo

# provide the url to connect with the client
client = pymongo.MongoClient("mongodb+srv://<Email>:<password>@cluster0.fnzozwe.mongodb.net/?retryWrites=true&w=majority")

# Database name
dataBase = client["my_database"]

# Collection name
collection = dataBase['my_collection']

# data declaration for collection
d= {'Name':'Raj Verma',
    'Age': 18,
    'City':'Indore'}

# insert above record in the collection
rec = collection.insert_one(d)

# Verify all the records present with all the fields
all_rec = collection.find()

# printing all the records present in the collection
for i, record in enumerate(all_rec):
    print(f"{i}:{record}")
