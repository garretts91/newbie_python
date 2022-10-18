available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break
else:
    print("Aren't you glad you got out of there?")

#A for loop will repeat for each item in a predetermined sequence, whereas with a while loop you don't need to know how many times the loop will execute
#One application of this is reading data from a file, or an internet stream
#A while loop can be used to keep reading until there is no more data left