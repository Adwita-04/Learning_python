year=input("Please provide a year:")

if  year.isdigit() and len(year)==4:
    year=int(year)
    if (year%4==0 and year%100 !=0) or  (year%400==0):
        print("It is a leap year")

    else:
        print("It is not a leap year")


else:
    print("please provide a valid year")

