"""TODO: Describe your scene program."""
 
__author__ = "Your PID"
 
from turtle import Turtle, colormode, done 
 
 
def main() -> None:
    """My scene is a house on an island with flowers and surrounded by water."""
    bing: Turtle = Turtle()
    bing.speed(0)
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    draw_square(bing, -50, 100, 100)
    draw_line(bing, -25, 0, 90, 50, "black")
    draw_line(bing, 25, 0, 90, 50, "black")
    draw_arc(bing, -25, 50, -90, 25, "black")
    tempx: float = -310.0
    tempy: float = -200
    for i in range(34):
        draw_arc(bing, tempx, tempy, 90, 10.0, "blue")
        tempx += 20
    draw_arc(bing, -200, -200, -90, 200, "green")
    draw_flower(bing, 30, 0, 2)
    
    done()
 
# TODO: Define the procedures for other components in your scene here.
 
def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1

def draw_line(a_turtle: Turtle, x:float, y: float, angle: float, length: float, color: str) -> None:
    """Draw a straight line, with input deciding color, start/stop, and heading"""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(angle)
    a_turtle.color(color)
    a_turtle.pendown()
    a_turtle.forward(length)

def draw_arc(a_turtle: Turtle, x: float, y: float, angle: float, radius: float, color: str) -> None:
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.color(color)
    a_turtle.setheading(angle)
    a_turtle.pendown()
    a_turtle.circle(radius, -180)

def draw_bit(a_turtle: Turtle, x: float, y: float) -> None:
    a_turtle.pendown()
    a_turtle.color("red", "pink")
    a_turtle.begin_fill
    a_turtle.circle(20, 360)
    a_turtle.left(120)
    a_turtle.circle(20, 360)
    a_turtle.left(90)
    a_turtle.end_fill

def draw_flower(a_turtle: Turtle, x: float, y: float, bits: int) -> None:
    a_turtle.penup()
    a_turtle.goto(x, y)
    if bits != 0:
        draw_bit(a_turtle, x, y)
        draw_flower(a_turtle, bits - 1, x - 50, y - 50)
        


# TODO: Use the __name__ is "__main__" idiom shown in class

#if __name__ is "__main__":
main()