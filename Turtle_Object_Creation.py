import turtle
t = turtle.Pen()

# Shape
# Size
# Coordinates

class Shape:
    def __init__(self, length, width, color, sides):
        self.length = length
        self.width = width
        self.color = color
        self.sides = sides

    def draw(self):
        t.width(4)
        angle = 360 / self.sides
        t.color(self.color)

        for i in range(self.sides):
            t.forward(self.length)
            t.right(angle)

    def turtleShapeChoice(self):
        shape_choice = int(input("""Please select a shape for your turtle pen:
1: Arrow
2: Turtle
3: Circle
4: Square
5: Triangle
6: Classic\n"""))

        if shape_choice == 1:
            t.shape("arrow")
        elif shape_choice == 2:
            t.shape("turtle")
        elif shape_choice == 3:
            t.shape("circle")
        elif shape_choice == 4:
            t.shape("square")
        elif shape_choice == 5:
            t.shape("triangle")
        elif shape_choice == 6:
            t.shape("classic")
        else:
            exit

    def coordinates(self):
        x_axis = int(input("Please choose an x coordinate for you shape: "))
        y_axis = int(input("Please choose a y coordinate for your shape: "))
        t.penup()
        t.setx(x_axis), t.sety(y_axis)
        t.pendown()

square = Shape(100, 100, "blue", 4)
triangle = Shape(100, 100, "pink", 3)
hexagon = Shape(80, 80, "purple", 6)
circle = Shape(1, 1, "orange", 360)

# square.draw()
# triangle.draw()
# hexagon.draw()
# circle.draw()

while True:

    user_interaction = int(input("""What would you like to draw?
1: Square
2: Triangle
3: Hexagon
4: Circle
5: Exit\n"""))


    if user_interaction == 1:
        square.turtleShapeChoice()
        square.coordinates()
        square.draw()

    elif user_interaction == 2:
        triangle.turtleShapeChoice()
        triangle.coordinates()
        triangle.draw()

    elif user_interaction == 3:
        hexagon.turtleShapeChoice()
        hexagon.coordinates()
        hexagon.draw()

    elif user_interaction == 4:
        circle.turtleShapeChoice()
        circle.coordinates()
        circle.draw()

    elif user_interaction == 5:
        break
    else:
        break

