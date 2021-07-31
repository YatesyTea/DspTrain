import json

# Setting Files to take and clean from and send to.
priorFile = 'formatted_recipes.json'
postFile = 'cleanedRecipes.json'

# Opening the file
with open(priorFile) as read_file: 
    data = json.load(read_file)

    # Going through data and removing Null value'd fat recipes.
    for recipe in data:
        if recipe['fat'] == None:
            del recipe
        
        elif recipe['protein'] == None:
            del recipe

        elif recipe['calories'] == None:
            del recipe

        elif recipe['sodium'] == None:
            del recipe

        elif recipe['ingredients'][0] == None or recipe['directions'][0] == None:
            del recipe

        else:
            # Open file to write to to read contents
            with open(postFile, 'r') as file:
                tempData = json.load(file)

            # Append    
            tempData.append(recipe)
            
            # Write back into file
            with open(postFile, 'w') as file:
                json.dump(tempData, file)