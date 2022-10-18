#strings are a sequence data type
parrot= "Norwegian Blue"
print(parrot)
print(parrot[10])
print(parrot[11])
print(parrot[12])
print(parrot[13])
#bracket is an index

#negative indexing in strings
print()
print(parrot[-11])  #Can think of it as 3 - 14 as well (index - string number count)
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
#negative indexing starts at 1 not 0

#slicing                #slicing is great for lists
print()
print(parrot[0:9])      #Norwegian - Last Character is not included in the slice (Up to, not including - Character 0 up to, not including 9)
print(parrot[10:14])    #Blue
print(parrot[:14])      #Norwegian Blue - If you start at index 0, you do not have to include the zero in the slice
print(parrot[10:])      #Blue - Same as before, but starting at a specified index to the end of the string
print(parrot[:6] + parrot[6:])
print(parrot[:])

#slicing with negative numbers
#you cant code backwards from the starting position (i.e. print(parrot([-4:2])); in other words, it will not write the string from right to left
print(parrot[-4:-2])
print(parrot[-4:12])    #you can code forwards with negative indeces 
print(parrot[-14:14])

#using a step in a slice
print(parrot[0:6:2])        #Nre - Starts at zero, up to six, in steps of two
print(parrot[0:12:3])       #Nwi - Starts at zero, up to twelve, in steps of three

number = "9,123;456:789 234,645;756"
#print(number[1::4])         #Start:Stop:Step - Started at index 1, with no stop until end of string, in steps of four
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val)for val in values])

name = "Sasquatch"
age = 94
print(age)

age_in_words = "Ninety Four"
print(name + f" is {age} years old")        #f string - formatted string literals (Does not work in Python 3.4 and earlier)
print(type(age))                            #f string and {age} works like a replacement field

print(f"Pi is approximately {22/7:12.50f}")
pi = 22/7
print(f"Pi is approximately {pi:12.50f}")
