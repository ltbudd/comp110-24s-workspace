#amount: float = 1.0
#if amount == 2.0:
#    print("You have 2!")
#else:
#    amount = amount + 1
#    if amount < 3.0:
#        print("Less than 3!")
#    else:
#        print("At least 3!")
#print(str(amount))

#x = type(9 / len( str(110)))
#print(x)
#y = len(str(110))
#print(y)
#z = 9/y
#print(z)

# age: int = int(input("What is your age?"))
# if age <= 12:
#     price: int = 5
# elif age <= 60:
#     price: int = 10
# print(price)

# x: list[float] = [1.0, 2.0]
# y: list[float] = [3.0, 4.0]
# y = x
# x[0] = 3.0
# print(x)
# print(y)

# def double(x: int) -> int:
#     return x * 2

# def double_display(y: int):
#     print(y * 2)

# double_display(2)
    
# if __name__ == "__main__":
#     print(double(3))

#def odd_and_even(a:list[int]) -> list[int]:
#    b:list[int] = list()
#    for i in range(len(a)):
#        if i%2 == 0:
#            if a[i] % 2 != 0:
#                b.append(a[i])
#    return(b)
#print(odd_and_even([2,3,4,5]))

import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(1)

# Move turtle to the starting point
t.penup()
t.goto(0, -100)  # Adjust the y-coordinate according to the desired radius
t.setheading(270)
t.pendown()

# Draw the bottom half of the semicircle
radius = 100
t.circle(radius, 180)  # Negative angle to draw in the opposite direction

# Keep the window open until it's closed manually
turtle.mainloop()