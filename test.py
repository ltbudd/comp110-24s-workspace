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

age: int = int(input("What is your age?"))
if age <= 12:
    price: int = 5
elif age <= 60:
    price: int = 10
print(price)