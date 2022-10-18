import random

highest = 1000
answer = random.randint(1, highest)
print(answer)   #TODO: Remove after testing
guess = 0       #Initialize to any number that doesn't equal the answer
print("Guess a number between 1 and {}: ".format(highest))


while guess != answer:
    guess = int(input())
    
    if guess == 0:
        break
    if guess == answer:
        print("Well done! You got it")
        break
    else:
        if guess < answer:
            print("Higher")
        else:   #guess must be greater than answer
            print("Lower")


print("The correct number was " + f"{answer}")

# if guess < answer:
#     print("Higher")
#     guess = int(input())
#     if guess == answer:
#         print("You got it!")
#     else:
#         print("Sorry")
# elif guess > answer:
#     print("Lower")
#     guess = int(input())
#     if guess == answer:
#         print("You got it!")
#     else:
#         print("Sorry")
# else:
#     print("You got it!")


# tree1 = "Spruce"
# tree2 = "Fir"
# if tree1 == tree2:
#     print("These trees are the same")
# else:
#     print("The trees are different")

# x = 5
# y = 7

# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# else:
#     print("x equals y")