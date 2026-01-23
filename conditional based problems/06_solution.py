order_size=input("provide your need of coffee:")
extra_shot=input("Do you want extra shot of expresso:")
if extra_shot=="yes":
    extra_shot=True
else:
    extra_shot=False

if extra_shot:
    coffee=order_size+" "+"coffee with extra shot"

else:
    coffee=order_size

print(coffee)