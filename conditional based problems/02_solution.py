age=int(input("please enter an age:"))
day=input("please enter the day name:")

price=12 if age>=18 else 8

if day=="Wednesday":
    price-=2

print("Ticket price for you is $",price)