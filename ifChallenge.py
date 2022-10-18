name = input("What is your name?: ")
age = int(input("How old are you, {0}? ".format(name)))

if 18 <= age < 31:
    print("Come on holiday with us, {0}!".format(name))
else:
    print("Sorry {0}, you cannot come on holiday with us".format(name))
