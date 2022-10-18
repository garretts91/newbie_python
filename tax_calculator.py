import time

while True:

    filing_status = int(input("Please enter your filing status (1-5):\n1: Single \n2: Married Filing Jointly \n3: Married Filing Separately \n4: Head of Household \n5: Exit\n"))

    if filing_status == 1:
        print("Filing taxes as Single")
        gross_income = int(input("Please enter your Adjusted Gross Income: "))
        if gross_income in range(0, 10275):
            print("Your tax bracket is 10%")
            break
        elif gross_income in range(10276, 41775):
            print("Your tax bracket is 12%")
            break
        elif gross_income in range(41776, 89075):
            print("Your tax bracket is 22%")
            break
        elif gross_income in range(89076, 170050):
            print("Your tax bracket is 24%")
            break
        elif gross_income in range(170051, 215950):
            print("Your tax bracket is 32%")
            break
        elif gross_income in range(215951, 539900):
            print("Your tax bracket is 35%")
            break
        elif gross_income > 539900:
            print("Your tax bracket is 37%")
            break
    elif filing_status == 2:
        print("Filing as Married Filing Jointly")
        gross_income = int(input("Please enter your Adjusted Gross Income: "))
        if gross_income in range(0, 20550):
            print("Your tax bracket is 10%")
            break
        elif gross_income in range(20551, 83550):
            print("Your tax bracket is 12%")
            break
        elif gross_income in range(83551, 178150):
            print("Your tax bracket is 22%")
            break
        elif gross_income in range(178151, 340100):
            print("Your tax bracket is 24%")
            break
        elif gross_income in range(340101, 431900):
            print("Your tax bracket is 32%")
            break
        elif gross_income in range(431901, 647850):
            print("Your tax bracket is 35%")
            break
        elif gross_income > 647850:
            print("Your tax bracket is 37%")
            break
    elif filing_status == 3:
        print("Filing as Married Filing Separately")
        gross_income = int(input("Please enter your Adjusted Gross Income: "))
        if gross_income in range(0, 10275):
            print("Your tax bracket is 10%")
            break
        elif gross_income in range(10276, 41775):
            print("Your tax bracket is 12%")
            break
        elif gross_income in range(41776, 89075):
            print("Your tax bracket is 22%")
            break
        elif gross_income in range(89076, 170050):
            print("Your tax bracket is 24%")
            break
        elif gross_income in range(170051, 215950):
            print("Your tax bracket is 32%")
            break
        elif gross_income in range(215951, 323925):
            print("Your tax bracket is 35%")
            break
        elif gross_income > 323925:
            print("Your tax bracket is 37%")
            break
    elif filing_status == 4:
        print("Filing as Head of Household")
        gross_income = int(input("Please enter your Adjusted Gross Income: "))
        if gross_income in range(0, 14650):
            print("Your tax bracket is 10%")
            break
        elif gross_income in range(14651, 55900):
            print("Your tax bracket is 12%")
            break
        elif gross_income in range(55901, 89050):
            print("Your tax bracket is 22%")
            break
        elif gross_income in range(89051, 170050):
            print("Your tax bracket is 24%")
            break
        elif gross_income in range(170051, 215950):
            print("Your tax bracket is 32%")
            break
        elif gross_income in range(215951, 539900):
            print("Your tax bracket is 35%")
            break
        elif gross_income > 539900:
            print("Your tax bracket is 37%")
            break
    elif filing_status == 5:
        break
    elif filing_status != 12345:
        print("Please choose a choice from 1 through 5")
        time.sleep(1)
    else:
        break