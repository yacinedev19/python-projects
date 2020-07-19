import turtle
terry = turtle.Turtle()
terry.width(10)
terry.penup()
terry.back(100)
terry.pendown()
for lines in ["red", "orange", "yellow", "green", "blue", "purple"]:
    for star in [1, 2, 3, 4, 5]:
        terry.color(lines)
        terry.forward(50)
        terry.right(145)
    terry.penup()
    terry.forward(110)
    terry.right(55)
    terry.pendown()
