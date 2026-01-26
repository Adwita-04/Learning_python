import math

def circle_states(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    return area,circumference

a,c=circle_states(int(input("provide a number:")))
print("Area:",round(a, 2),"Circumference:",round(c, 2))