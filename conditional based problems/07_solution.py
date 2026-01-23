password=len(input("Please provide your password:"))

if password<6:
    print("Password strength:Weak")

elif password>=6 and password<=10:
    print("Password strength:Medium")

else:
    print("Password strength:Strong")