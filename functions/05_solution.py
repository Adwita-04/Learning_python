def greet(name="rakshita"):
    return "Hello"+" "+name+"!"

a=input("Please provide a name:")
if a=="":
    print(greet())
else:
    print(greet(a))
