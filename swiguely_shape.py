import turtle
t = turtle.Turtle()
t.color("black")
t.width(3)
t.speed(0)
t.hideturtle()

def square(number):
    return number * number

for n in range(540):
    angle = square(n)
    t.right(angle + .5)
    t.forward(5)