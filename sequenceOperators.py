#Sequence Operators
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"
print(string1 + string2 + string3 + string4 + string5)

print("Hello " * 5)
#print("Hello " * 5 + 4)        #you can only concatenate str (not int) to string

print("Howdy " * (5 + 4))       #remember order of operations
print("Howdy " * 5 + "4")       #appends the four to the end of the string

today = "saturday"
print("day" in today)           #in is a boolean
print("rob" in string2)
print("turd" in today)
print("knight" in string5)