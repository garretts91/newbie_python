phone_book = {}
#create an empty map

for i in range(3):
    #use a for loop to iterate over a certain range, in this case 3
    #you can change the number to however many names and numbers you want to input
    name = input("Please enter a name: ")
    phone_number = input("Please enter their phone number: ")

    phone_book[name] = phone_number

print(phone_book)
#show the current map of who is listed

name_look_up = input("Please enter a name to lookup: ")
print("%s's phone number is: %s" % (name_look_up, phone_book[name_look_up]))
#look up a name in the map
phone_book[name] = phone_number
phone_book[phone_number] = name
#used for reverse lookup so names point at their numbers & vice versa
rev_lookup = input("Please enter a phone number to lookup: ")
print("That is %s's phone number." % (phone_book[phone_number]))
