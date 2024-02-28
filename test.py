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

def double(x: int) -> int:
    return x * 2

def double_display(y: int):
    print(y * 2)

double_display(2)
    
if __name__ == "__main__":
    print(double(3))