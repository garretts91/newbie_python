from re import A


parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
#String comparisons are case sensitive
