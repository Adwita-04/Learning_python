current_weather=(input("provide the current weather name:")).lower()

if current_weather=="sunny":
    print("Activity:Go for a walk")

elif current_weather=="rainy":
    print("Activity:Read a book")

elif current_weather=="snowy":
    print("Activity:Build a snowman")

else:
    print("Provide a valide weather name")