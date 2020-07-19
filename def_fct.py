import turtle

# Write a function here that creates a
# turtle and draws a shape with it.
def triangle(color, start):
    laid = turtle.Turtle()
    laid.width(5)
    laid.speed(0)
    laid.color(color)
    laid.right(start)
    for tri in range(6):
        for sides in range(3):
            laid.forward(100)
            laid.right(120)
        laid.right(15)
    laid.hideturtle()
# Call the function multiple times.
triangle("red", 0)
triangle("orange", 120)
triangle("blue", 240)