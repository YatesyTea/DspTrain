import pymongo

# Connect to the recipes database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipeDB"]
mycol = mydb["recipes"]

# Fat content higher than 50
myquery = {{ "fat": {"$gt": 50} }}

mydoc = mycol.find(myquery)

for recipe in mydoc:
  print(f"Fat: {recipe['fat']}\n")