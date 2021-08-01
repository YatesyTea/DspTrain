import json

# Opening the file
with open('cleanedRecipes.json') as read_file: 
    data = json.load(read_file)
    x=0
    for recipe in data:
        x+=1
    print(x)