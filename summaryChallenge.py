#challenge_options = ["1: Learn Python \n2: Watch a movie \n3: Make a sandwich \n4: Play Magic \n5:  6, 7, 8, 9 , 0: Exit"]
choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose an option between 0 and 5:")
        print("1: Learn Python") 
        print("2: Watch a movie")
        print("3: Make a sandwich")
        print("4: Go fishing")
        print("5: Go workout")
        print("0: Exit")
    
    choice = input()