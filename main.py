import math
from os import name, system
from time import sleep


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


diameter = 1.0
circumference = 1.0
area = 1.0
case = 1
reask = "0"

while True:
    try:
        case = int(input("Type '1' for area or type '2' for circumference: "))
        if case == 1:
            diameter = int(input("What's the diameter of the circle? "))
            print("Diameter:", diameter)
            radius = int(diameter // 2)
            print("Radius:", radius)
            area = round((math.pi * radius ** 2), 2)
            print("Area of the circle is:", area)
        elif case == 2:
            diameter = int(input("What's the diameter of the circle? "))
            print("Diameter:", diameter)
            radius = int(diameter // 2)
            print("Radius:", radius)
            circumference = round((2 * math.pi * radius), 2)
            print("Circumference of the circle is:", circumference)
        else:
            print("Please input a real option")
    except ValueError:
        print("Please input a number!")
    while True:
        reask = str(input("New Calculation? (y/n): "))
        if reask in ("y", "n"):
            break
        print("invalid input.")
    if reask == "y":
        sleep(1)
        clear()
        continue
    else:
        sleep(0.5)
        print("Goodbye. Thanks for calculating!")
        break
