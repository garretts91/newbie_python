print("Python was created by Guido van Rossum.")
print("He's referred to as the BDFL,")
print("the 'Benevolent Dictator For Life'")
print("and has the final word when it comes to enhancements to Python.")

meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
eggs
beans"""

print(meal1)
print(meal2)
print(meal3)
print(meal4)

print("Terry\tJohn\tGraham\tMichael\tEric\tTerry")

first_name = "John"
last_name = "Cleese"
age = 78
 
print(first_name + last_name + f"{age}")

a = 45
b = 15
c = 3
 
print(a - b / c)

quantity = 10
price = 5.0
total = quantity * price
tax = total / 5
 
Total = total + tax
 
print(total)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])

flower = "blue violet"
print('blue' in flower)

flower = "rose"
color = "red"
print("The {0} is {1}".format(flower, color))