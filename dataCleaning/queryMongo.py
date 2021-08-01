import pymongo

# Connect to the recipes database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipeDB"]
mycol = mydb["recipes"]

# Return a singular recipe
x = mycol.find_one()

print(x) 