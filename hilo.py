low = 1
high = 1000

print("Please think of a number between {} and {}.".format(low, high))
input("Press ENTER to start")

guesses = 1

while low != high:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2         #binary search algorithm
    high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct. ".format(guess)).casefold()

    if high_low == "h":
        #Guess higher
        #pass
        low = guess + 1
    elif high_low == "l":
        #Guess lower
        #pass
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, or c")
    #guesses = guesses + 1  #augmented assignment -> the addition is the binary operation (binary b/c it takes 2 operands to work on) and then there is an assignment
    guesses += 1            #look up augmented assignments (+, -, /, *, **, etc.)
else:
    print("You though of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))