"""
DICE
RANDOM FACE NUMBER
LOOPING

develop random number
check the number
print the face 
looping

"""

import random
print("THIS IS A DICE STIMULATOR")



x="y"
while x=="y" or "Y":
    number=random.randint(1,6)

    if number==1:
        print("--------------")
        print("|            |")
        print("|            |")
        print("|    0       |")
        print("|            |")
        print("|            |")
        print("--------------")
    if number==2:
        print("--------------")
        print("|  0         |")
        print("|            |")
        print("|            |")
        print("|            |")
        print("|        0   |")
        print("--------------")
    if number==3:

        print("--------------")
        print("| 0          |")
        print("|            |")
        print("|    0       |")
        print("|            |")
        print("|         0  |")
        print("--------------")
    if number==4:
        print("--------------")
        print("|  0       0 |")
        print("|            |")
        print("|            |")
        print("|            |")
        print("|  0       0 |")
        print("--------------")
    if number==5:
        print("--------------")
        print("|  0       0 |")
        print("|            |")
        print("|     0      |")
        print("|            |")
        print("|  0       0 |")
        print("--------------")

    if number==6:
        print("--------------")
        print("|  0       0 |")
        print("|            |")
        print("|  0       0 |")
        print("|            |")
        print("|  0       0 |")
        print("--------------")
    x=input("Enter y to roll the dice")