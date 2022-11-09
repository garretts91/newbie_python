shape_options = int(input("""Please Select A Shape From the Options Below:
1: Rocket
2: Kirby
3: Happy Face
4: Winky Face
5: Boxer Kirby
6: Exit Program
"""))

rocket = " >>---> "
kirby = " <('o'<) "
happy_face = " (^.^) "
winky_face = " (-.^) "
boxing_kirby = " Q('.'O) "

if shape_options == 1:
        print(rocket)
        quantity = int(input("How many times would you like the shape repeated?: "))
        if quantity > 10:
            print("Please select a lower number. ")
        else:
            for i in range (0, quantity):
                print((rocket * quantity))
                break
elif shape_options == 2:
        print(kirby)
        quantity = int(input("How many times would you like the shape repeated?: "))
        if quantity > 10:
            print("Please select a lower number. ")
        for i in range (0, quantity):
            print((kirby * quantity))
            break
elif shape_options == 3:
        print(happy_face)
        quantity = int(input("How many times would you like the shape repeated?: "))
        if quantity > 10:
            print("Please select a lower number. ")
        for i in range (0, quantity):
            print((happy_face * quantity))
            break
elif shape_options == 4:
        print(winky_face)
        quantity = int(input("How many times would you like the shape repeated?: "))
        if quantity > 10:
            print("Please select a lower number. ")
        for i in range (0, quantity):
            print((winky_face * quantity))
            break         
elif shape_options == 5:
        print(boxing_kirby)
        quantity = int(input("How many times would you like the shape repeated?: "))
        if quantity > 10:
            print("Please select a lower number. ")
        for i in range (0, quantity):
            print((boxing_kirby * quantity))
            break    
elif shape_options == 6:
    print("Goodbye.")
    exit
else:
    exit
    
# <('o'<) ^( '-' )^ (>'o')> v( '.' )v <(' .' )> <('.'<) ^( '.' )^ (>'.')> v( '.' )v <(' .' )>
# Q('.'O)

# except ValueError:
#         print("Invalid integer, please select a lower number.")
    # for i in range (0, quantity):
    #     print(Square)
# elif shape_options == 4:
#     print(Rectangle)
#     quantity = int(input("How many times would you like the shape repeated?: "))
#     for i in range (0, quantity):
#         print(Rectangle)