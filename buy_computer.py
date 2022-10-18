available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Speaker",
                   "HDMI Cable",
                   "External Storage" 
                   ]
#You can add or delete however many items, and the program should work
#valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

customer_choice = "-"
computer_parts = []         #create an empty list

while customer_choice != '0':
    if customer_choice in valid_choices:
        print("adding {}".format(customer_choice))
        index = int(customer_choice) - 1
        customer_choice = available_parts[index]
        computer_parts.append(customer_choice)
    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))      #{0} index position, {1} item -Number is index position, part is item from list

    customer_choice = input()

print(computer_parts)