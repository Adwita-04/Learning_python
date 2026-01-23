score=int(input("please provide your score:"))

if score>=101:
     print("Please verify your score again")
     exit()

if score>=90 and score<=100:
    print("You were awarded an A grade")

elif score>=80 and score<=89:
    print("You were awarded an B grade")

elif score>=70 and score<=79:
    print("You were awarded an C grade")

elif score>=60 and score<=69:
    print("You were awarded an D grade")

elif score<60:
    print("You were awarded an F grade")