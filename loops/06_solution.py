n=int(input("provide a number:"))
factorial=1

while n>0:
    factorial=factorial*n
    n-=1

print("factorial of",n,'is:',factorial)