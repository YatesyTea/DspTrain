import json

# Opening the file
with open('test.json') as read_file: 
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
            with open('cleanedTest.json', 'r') as file:
                tempData = json.load(file)

            # Append    
            tempData.append(recipe)
            
            # Write back into file
            with open('cleanedTest.json', 'w') as file:
                json.dump(tempData, file)