import random


def main():
    print("Dice Roller")
    going = True
    temp = input("Roll the dice? (y/n): ")
    if temp == "n":
        going = False
    while going:
        diceRoll()
        temp = input("Roll again? (y/n): ")
        if temp == "n":
            going = False


def diceRoll():
    roll1 = rollDie()
    roll2 = rollDie()
    total = roll1 + roll2
    print("Die 1: " + str(roll1))
    print("Die 2: " + str(roll2))
    print("Total: " + str(total))
    if roll1 == 1 and roll2 == 1:
        print("Snake eyes!")
    if roll1 == 6 and roll2 == 6:
        print("Boxcars!")


def rollDie():
    return random.randint(1, 6)


main()
