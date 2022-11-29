import turtle

with open('stockIndex.csv','r') as csvfile:
    lines = csvfile.readlines()
n = len(lines)-1
prices = [None]*n
for i in range(1,len(lines)):
    row = lines[i].split(',')
    prices[i-1] = float(row[1])
minprice, maxprice = min(prices),max(prices)

screen = turtle.Screen()
# screen.title("")
screen.setup(800,600)
screen.setworldcoordinates(0,minprice*0.9,n,maxprice*1.1)
# turtle.speed(0)
turtle.hideturtle()
turtle.up()
turtle.goto(0,prices[0])
turtle.down()
for i in range(1,n):
    turtle.goto(i,prices[i])

turtle.exitonclick()
