# result = True
# another_result = result
# print(id(result))
# print(id(another_result))

# #Python docs - functions - id
# #id returns the identity of an object
# #The id for an object may be different each time you run the program, but while your program is running, the object will have the same id

# result = False
# print(id(result))

# #result is rebound to a new value, in this case, false

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

#augmented assignment
result += "ish"
print(id(result))
print(id(another_result))