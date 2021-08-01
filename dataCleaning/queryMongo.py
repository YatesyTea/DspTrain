import pymongo

# Connect to the recipes database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipeDB"]
mycol = mydb["recipes"]

# Fat content within range
myquery = {"fat" : {"$gte": 20,"$lte": 21}}

mydoc = mycol.find(myquery)

for x in mydoc:
  print(f"Fat: {x['fat']}")