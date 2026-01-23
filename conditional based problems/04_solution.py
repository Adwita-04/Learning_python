fruit_color=(input("What is the color of the Fruit?:")).upper()

if fruit_color=="GREEN":
    print("Unripe")

elif fruit_color=="YELLOW":
    print("Ripe")

elif fruit_color=="BROWN":
    print("Overripe")

else:
    print("Provide a valid color of the fruit")