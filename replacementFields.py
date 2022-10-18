age = 31
print("My age is {0} years".format(age))        #Curly brace is a replacement field

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
    .format(31, "January", "March", "May", "July", "August", "October", "December"))

#8 replacement fields, 0-7

print("There are {0} days in January, March, May, July, August, October and December".format(31))

#Number in the curly braces corresponds to the value associated with it

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}."
    .format(28, 30, 31))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}
""".format(28, 30, 31))