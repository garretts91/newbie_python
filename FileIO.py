import csv
import turtle
t=turtle.Pen()

shipData = []
print("Contents of shipAltSize ")
# Make sure filename and location are accessible and correct
#In this file, column 1 is ship name, column 2 is altitude, column 3 is ship size
with open("ShipAltSize.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        print(row)
        shipData.append(row)

print("\nContents of shipData: ")
print(shipData)

t.width(10)
t.circle(-50)
for row in shipData:
    print("row[0] is", row[0])
    print("size is ", row[2])
    t.up()
    t.goto(0, int(row[1]))
    t.down()
    t.forward(int(row[2]))
    t.write(row[0])

print(turtle.screensize())
turtle.exitonclick()