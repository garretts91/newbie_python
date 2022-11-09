#python style guide for lists, PEP8
#look at trailing commas in the style guide as well
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
#write code to print out all the meals in the menu, but with spam removed
#You can:
    #Remove spam from each list, then print the list
    #Print out the items in each list, as long as it's not spam
#Remember: produce eight meals, all without spam

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(meal)

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item)
    
#     print()