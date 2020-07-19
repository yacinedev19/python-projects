import turtle
t = turtle.Turtle()
t.color("cyan")
t.speed(0)
t.width(5)
for side in range(80):
    t.forward(side * 10)
    t.right(120)