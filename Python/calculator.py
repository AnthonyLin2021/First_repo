
import math

shape = int(input('================== \n Area Calculator 📐\n==================\n\n ' \
'1) Square\n 2) Rectangle\n 3) Triangle\n 4) Circle\n 5) Quit \n'))

if shape==1:
    print("Which shape: 1\n")
    side = float(input("Side: "))
    area = side*2
    print(f"\nThe area is {area}")
elif shape ==2:
    print("Which shape: 2")
    length= float(input("Length:"))
    width = input(input("Width: "))
    area = length * width
    print(f"The area is {area}")
elif shape ==3:
    print("Which shape: 3")
    base= float(input('Base: '))
    height = float(input('Height: '))
    area = height*base/2
    print(f"\nThe area is {area}")
elif shape ==4:
    print("Which shape: 4")
    radius= float(input("Radius: "))
    area = radius**2 * math.pi
    print(f"\n The area is {area}")
elif shape ==5:
    print("Exiting")
else:
    print("Invalid input" )
    shape = int(input('================== \n Area Calculator 📐\n ==================\n\n ' \
    '1) Square\n 2) Rectangle\n 3) Triangle\n 4) Circle\n5)Quit'))

