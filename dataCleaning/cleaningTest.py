import json

# Opening the file
with open('test.json') as read_file: 
    data = json.load(read_file)

    for recipe in data:
        del recipe['date']
        del recipe['rating']
                

        # print(f"Title: {recipe['title']} \n Calories: {recipe['calories']} \n Sodium: {recipe['sodium']} \n Fat: {recipe['fat']} \n Protein: {recipe['protein']} \n\n")