import turtle

t = turtle.Turtle()
t.color("lime")
t.width(3)
t.penup()
t.shape("turtle")

for step in range(2000):
    t.forward(1)
    if t.xcor() > 100 or t.xcor() < -100:
        t.right(30)
