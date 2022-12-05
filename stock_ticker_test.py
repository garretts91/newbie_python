import turtle

print("Reading file into list...")
with open('stockIndex.csv','r') as csvfile:
    lines = csvfile.readlines()
    # https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
    # lines is assigned to read the stockIndex file, and readlines will read each line of the file
x = len(lines)-1
# x is assigned as the representation of the x-axis (days) which is the amount of lines the csvfile has total
prices = [None]*x
# prices is assigned as a list that will be multiplied by x, which is the length of the total lines of the csvfile
# None is required in the list because it is being treated as a placeholder for the elements in the list
# https://docs.python.org/3/library/constants.html?highlight=none#None

for i in range(1,len(lines)):
    row = lines[i].split(',')
    # row is iterating over each row of values at index 0 and 1, and needs the comma to be split because it is a string instead of an int/ float
    # https://docs.python.org/3/library/stdtypes.html?highlight=str%20split#str.split
    prices[i-1] = float(row[1])
    # prices will be called upon as index 1 in the row variable
print("The data in the list...")
print(lines)
# print the data into the terminal, the \n appears because of the built-in function .readlines()

def screenParameters():
    screen = turtle.Screen()
    screen.title("Stock Index")
    screen.setup(800,600)
    #setup = size of screen
    screen.setworldcoordinates(-5,-30,35,200)
    # https://docs.python.org/3/library/turtle.html#turtle.setworldcoordinates
    # set world coordinates: x coord of lower left, y coord of lower left; x, y upper right
    # visible world = [-5, -30], [35, 200]

print("Drawing the graph...")
def colorIterator():
    # this is going to draw the rise and fall of the stocks
    turtle.width(3)
    turtle.hideturtle()
    turtle.up()
    turtle.goto(0, prices[0])
    # turtle will start at 0, and prices at index 0, which is the first index in the list (100)
    turtle.down()
    for i in range(0, x):
        if prices[i] > prices[i-1]:
            # if the prices are greater than the prices before it, color the line green
            turtle.color("green")
        else:
            turtle.color("red")
            # if the prices are not greater than the prices before it, then color the line red
        turtle.goto(i,prices[i])
        # iterate over the prices to draw the graph

# graph
# draw the x, y axis of the graph
def drawAxis():
    turtle.color("black")
    turtle.width(2)
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    turtle.goto(0, 180)
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    turtle.goto(30, 0)
    turtle.up()

# drawing the hash marks of the x-axis in a for loop
def xHash():
    turtle.up()
    turtle.speed(100)
    turtle.goto(0, 0)
    turtle.width(2)
    for j in range(30):
        # write the hash marks in a loop for the x-axis
        turtle.down()
        turtle.right(90)
        turtle.forward(2)
        turtle.left(180)
        turtle.up()
        turtle.forward(2)
        turtle.down()
        turtle.right(90)
        turtle.forward(1)
        

# This did not work how I wanted, but here we are:
# I wasn't able to find a good way to loop the y-axis hash marks, so I had to go hash by hash
def yHash():
    turtle.up()
    turtle.speed(10)
    turtle.goto(0, 0)
    turtle.width(2)
    turtle.down()
    turtle.goto(-.5, 0)
    turtle.goto(0, 0)
    turtle.goto(0, 10)
    turtle.goto(-.5, 10)
    turtle.goto(0, 10)
    turtle.goto(0, 20)
    turtle.goto(-.5, 20)
    turtle.goto(0, 20)
    turtle.goto(0, 30)
    turtle.goto(-.5, 30)
    turtle.goto(0, 30)
    turtle.goto(0, 40)
    turtle.goto(-.5, 40)
    turtle.goto(0, 40)
    turtle.goto(0, 50)
    turtle.goto(-.5, 50)
    turtle.goto(0, 50)
    turtle.goto(0, 60)
    turtle.goto(-.5, 60)
    turtle.goto(0, 60)
    turtle.goto(0, 70)
    turtle.goto(-.5, 70)
    turtle.goto(0, 70)
    turtle.goto(0, 80)
    turtle.goto(-.5, 80)
    turtle.goto(0, 80)
    turtle.goto(0, 90)
    turtle.goto(-.5, 90)
    turtle.goto(0, 90)
    turtle.goto(0, 100)
    turtle.goto(-.5, 100)
    turtle.goto(0, 100)
    turtle.goto(0, 110)
    turtle.goto(-.5, 110)
    turtle.goto(0, 110)
    turtle.goto(0, 120)
    turtle.goto(-.5, 120)
    turtle.goto(0, 120)
    turtle.goto(0, 130)
    turtle.goto(-.5, 130)
    turtle.goto(0, 130)
    turtle.goto(0, 140)
    turtle.goto(-.5, 140)
    turtle.goto(0, 140)
    turtle.goto(0, 150)
    turtle.goto(-.5, 150)
    turtle.goto(0, 150)
    turtle.goto(0, 160)
    turtle.goto(-.5, 160)
    turtle.goto(0, 160)
    turtle.goto(0, 170)
    turtle.goto(-.5, 170)
    turtle.goto(0, 170)
    turtle.goto(0, 180)
    turtle.goto(-.5, 180)
    turtle.hideturtle()
    turtle.up()
    turtle.goto(0, 0)    

# make a call to the earlier code to run them as functions defined by the methods
screenParameters()
colorIterator()
drawAxis()
xHash()
yHash()

# labeling the hash of the x-axis as well as labeling the graph
# x-axis starts at 1 because 1 is the first value given in the csv file
def labelMakerX():
    turtle.goto(-5, 90)
    turtle.write("Stock Index")
    turtle.goto(15, -20)
    turtle.write("Days")
    turtle.goto(0, -7)
    turtle.write("1")
    turtle.goto(4, -7)
    turtle.write("5")
    turtle.goto(8.75, -7)
    turtle.write("10")
    turtle.goto(13.75, -7)
    turtle.write("15")
    turtle.goto(18.75, -7)
    turtle.write("20")
    turtle.goto(23.75, -7)
    turtle.write("25")
    turtle.goto(28.75, -7)
    turtle.write("30")

# making the call to the function
labelMakerX()

# labeling the values of the hash marks on the y-axis
def labelMakerY():
    turtle.goto(-1, -3)
    turtle.write("0")
    turtle.goto(-1.25, 17.5)
    turtle.write("20")
    turtle.goto(-1.25, 37.5)
    turtle.write("40")
    turtle.goto(-1.25, 57.5)
    turtle.write("60")
    turtle.goto(-1.25, 77.5)
    turtle.write("80")
    turtle.goto(-1.5, 97.5)
    turtle.write("100")
    turtle.goto(-1.5, 117.5)
    turtle.write("120")
    turtle.goto(-1.5, 137.5)
    turtle.write("140")
    turtle.goto(-1.5, 157.5)
    turtle.write("160")
    turtle.goto(-1.5, 177.5)
    turtle.write("180")

# making the call to the function
labelMakerY()

#leaving the turtle program running, until the user clicks on the window to close it
turtle.exitonclick()