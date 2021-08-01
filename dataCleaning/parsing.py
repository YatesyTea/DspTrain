import json

# Opening the file
with open('cleanedRecipes.json') as read_file: 
    data = json.load(read_file)

    # Looping through Data
    x=0
    for recipe in data:
        x+=1

    print(x)
    # Formatting within LaTeX displays weird symbols for spaces within F-strings, this is likely due to lack of support within LaTeX for Python3.6 and higher and their usage of F-strings.