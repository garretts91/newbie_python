import turtle
t = turtle.Pen()

class Shape:
    def __init__(self, length, width, color, sides):
        self.length = length
        self.width = width
        self.color = color
        self.sides = sides

    def draw(self):
        import turtle
        t = turtle.Pen()
        t.width(5)
        angle = 360 / self.sides
        t.color(self.color)

        for i in range(self.sides):
            t.forward(self.length)
            t.right(angle)

square = Shape(100, 100, "blue", 4)
triangle = Shape(100, 100, "red", 3)
hexagon = Shape(80, 80, "yellow", 6)
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
        square.draw()

    elif user_interaction == 2:
        triangle.draw()

    elif user_interaction == 3:
        hexagon.draw()

    elif user_interaction == 4:
        circle.draw()

    elif user_interaction == 5:
        break
    else:
        break
