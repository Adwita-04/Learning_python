def factorial(n): 
    ans=n
    if n==0:
        return 1
    else:
  
     return ans*factorial(n-1)
    
result=factorial(int(input("provide a number:")))
print(result)