import pymongo

# Connect to the recipes database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipeDB"]
mycol = mydb["recipes"]

# Fat content higher than 20
myquery = { "fat": {"$gt": 50} }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)