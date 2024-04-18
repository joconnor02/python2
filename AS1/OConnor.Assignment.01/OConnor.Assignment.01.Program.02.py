def main():
    print("Hike Calculator")
    temp = float(input("How many miles did you walk?: "))
    print("You walked " + str(milesToFeet(temp)) + " feet.")


def milesToFeet(num):
    ret = int(num * 5280)
    return ret


main()
