import random


def oszto():
    vel = int(random.random() * 49) + 1
    print(vel)
    if vel % 5 == 0 and vel % 3 == 0:
        print("A szám öttel és hárommal is osztható")
    elif vel % 5 == 0:
        print("A szám öttel osztható!")
    elif vel % 3 == 0:
        print("A szám hárommal  osztható!")
    else:
        print("A szám nem osztható sem öttem sem hárommal!")
