import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipeDB"]
mycol = mydb["recipes"]

priorFile = 'cleanedRecipes.json'

# Opening the file
with open(priorFile) as read_file: 
    data = json.load(read_file)

x = mycol.insert_many(data)

#print list of the _id values of the inserted documents:
print(x.inserted_ids) 