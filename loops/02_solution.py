n=int(input("please provide a number:"))
even_sum=0

if n>0:
    for i in range(1,n+1):
        if i%2==0:
            even_sum+=i
    print(even_sum)

else:
    print("please provide a valid number")