# The following program is intended to print out a "times table" for the value 8.
value = 8
answer = 0
for x in range(1, 13):
    answer = value * x
    print("{0} times {1} is {2}".format(x, value, answer))
# The output should be:
# 1 times 8 is 8
# 2 times 8 is 16
# 3 times 8 is 24
# 4 times 8 is 32
# 5 times 8 is 40
# 6 times 8 is 48
# 7 times 8 is 56
# 8 times 8 is 64
# 9 times 8 is 72
# 10 times 8 is 80
# 11 times 8 is 88
# 12 times 8 is 96

# In a program for a taxi company, the code needs to decide if they should send a minibus instead of a taxi.
# A taxi can only carry 4 passengers, and a minibus can carry up to 14.
# Which of these if statements would result in a minibus being used only when necessary.
# people is the number of people booking transport.

# if 4 < people <= 14:
#     print("You need a minibus")

# Material comes in different widths.  We have material in 36 inch and 60 inch widths.
# Using material that's 36 inches wide, our dress pattern needs a length of 150 inches.  It only needs 80 inches of material that's 60 inches wide.
# Which of these conditions will correctly work out if we have enough material to make a dress?

# if width == 36 and length >= 150 or width == 60 and length >= 80:
#   print("Make a dress")

#Which of these programs will correctly print out the even numbers from 0 to 20 (inclusive)

for value in range(11):
    value *= 2
    print(value)

asteroids = [9617, 9618, 9619, 9620, 9621, 9622, 13681]
 
for asteroid in asteroids:
    if asteroid == 9617:
        print("Graham Chapman")
    elif asteroid == 9618:
        print("John Cleese")
    elif asteroid == 9619:
        print("Terry Gilliam")
        break
    elif asteroid == 9620:
        print("Eric Idle")
    elif asteroid == 9621:
        print("Michael Palin")
    else:
        print("Terry Jones")
else:
    print("Monty Python")

#Which program will produce the same output as:
for x in range(30):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)

for x in range(30):
    if x % 3 != 0 and x % 5 != 0:
        print(x)

# quote = """
# It's not pining. It's passed on. This parrot is no more. It has ceased to be.
# It's expired and gone to meet its maker.
# This is a late parrot.
# It's a stiff. Bereft of life, it rests in peace.
# If you hadn't nailed it to the perch, it would be pushing up the daisies.
# It's rung down the curtain and joined the choir invisible.
# THIS IS AN EX-PARROT.
# """

# period_count = 0
# for char in quote:
#     if char == '.':
#         period_count = period_count + 1
# print(period_count)

# period_count = 0
# for char in quote:
#     if char == ".":
#         period_count += 1

choice = None
 
while choice != '0':
    choice = input("Please enter your choice.  Press enter to quit")
    if choice == '':
        break
 
    print("You have selected {}".format(choice))
else:
    print("Thank you for playing, please call back soon.")