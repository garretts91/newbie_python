# day = "Friday"
# temperature = 30
# raining = False

# #All conditions must equal true in order for the boolean to come up as true
# #Remember the differences between and/or
# #Look at operator precedence in Python documentation
# #Always use parentheses when using and as well as or in the same condition to make the code more clear
# #and has a higher precedence than or

# if (day == "Saturday" and temperature > 27) or not raining:
#     print("Go swimming")
# else:
#     print("Learn Python")

if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name:
#if name != " ":
    print("Hello {}".format(name))
else:
    print("Are you the man with no name?")
