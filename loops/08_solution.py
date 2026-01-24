number=int(input("please enter a number :"))
is_prime=True

if number>1:
    for i in range(2,int(number**0.5)+1):
        if(number%i==0):
            is_prime=False
            break
print(is_prime)