import turtle

def spiral(sides, turn, color, width):
    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    t.speed(0)
    for n in range(sides):
        t.forward(n)
        t.right(turn)

spiral(300, 45, "red", 2)