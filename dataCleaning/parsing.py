import json

# Opening the file
with open('cleanedRecipes.json') as read_file: 
    data = json.load(read_file)

    # Looping through Data
    for recipe in data:
        print(f"Title: {recipe['title']} \n Calories: {recipe['calories']} \n Sodium: {recipe['sodium']} \n Fat: {recipe['fat']} \n Protein: {recipe['protein']} \n\n")
    # Formatting within LaTeX displays weird symbols for spaces within F-strings, this is likely due to lack of support within LaTeX for Python3.6 and higher and their usage of F-strings.