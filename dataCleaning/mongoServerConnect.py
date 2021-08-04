import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://dbUser:<FUCKMEAT5AMPlease>@cluster0.cisj1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
mycol = db.recipes

priorFile = 'cleanedRecipes.json'

# Opening the file
with open(priorFile) as read_file: 
    data = json.load(read_file)

x = mycol.insert_many(data)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)