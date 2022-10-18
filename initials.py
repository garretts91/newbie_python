import turtle
turtle.colormode(255)
turtle.title("Initials Fun")
turtle.bgcolor(30, 207, 223)
window = turtle.Screen()
my_turtle = turtle.Pen()
my_turtle.speed(5)
my_turtle.shapesize(3)
my_turtle.pensize(10)
my_turtle.pencolor((100, 0, 166))

my_turtle.penup()
my_turtle.goto(-150, 0)
my_turtle.pendown()

my_turtle.forward(45)
my_turtle.right(90)
for x in range(90):
    my_turtle.forward(2)
    my_turtle.right(2)

my_turtle.forward(25)

for x in range(75):
    my_turtle.forward(2)
    my_turtle.right(2)

my_turtle.penup()
my_turtle.goto(-85, 80)
my_turtle.pendown()

my_turtle.right(30)
my_turtle.forward(135)

my_turtle.penup()
my_turtle.goto(-85, 80)
my_turtle.pendown()

my_turtle.left(45)
my_turtle.forward(65)
my_turtle.left(90)
my_turtle.forward(65)
my_turtle.right(135)
my_turtle.forward(135)

my_turtle.penup()
my_turtle.goto(30, -50)
my_turtle.pendown()

my_turtle.left(45)
for x in range(135):
    my_turtle.forward(1)
    my_turtle.left(1.5)

my_turtle.forward(25)

for x in range(95):
    my_turtle.forward(1)
    my_turtle.right(2)

my_turtle.penup()
my_turtle.goto(90, 90)
my_turtle.pendown()
my_turtle.pen(pencolor=(255, 70, 0), pensize = 3)
my_turtle.shapesize(1)

n = 5
while n <= 40:
    my_turtle.circle(n)
    n = n + 5

for x in range(180):
    my_turtle.forward(2)
    my_turtle.right(1)

my_turtle.forward(70)

n = 25
while n >= 5:
    my_turtle.circle(n)
    n = n - 5

window.exitonclick()
