number = input("Please enter a series of numbers, using any separators you like: ")
#print(number[1::4])         #Start:Stop:Step - Started at index 1, with no stop until end of string, in steps of four
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val)for val in values]))

#python built in functions