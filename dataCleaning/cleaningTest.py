import json

# Setting Files to take and clean from and send to.
priorFile = 'formatted_recipes.json'
postFile = 'cleanedRecipes.json'

# Opening the file
with open(priorFile) as read_file: 
    data = json.load(read_file)

    # Going through data and removing Null value'd recipes.
    for recipe in data:

        important = ['fat', 'protein', 'calories', 'sodium', 'ingredients', 'directions']
        for key, value in recipe.items():
            if value == None and key in important:
                print(f'{key} None --> Deleted')
                del recipe
                break

        else:
            # Open file to write to to read contents
            with open(postFile, 'r') as file:
                tempData = json.load(file)

            # Append    
            tempData.append(recipe)
            
            # Write back into file
            with open(postFile, 'w') as file:
                json.dump(tempData, file)
            
            print(f"Added recipe {recipe} to database")