from as01part3module import metersToFeet, feetToMeters


def main():
    title()
    going = True
    while going:
        if menu():
            feet = input("Enter feet: ")
            temp = round(feetToMeters(feet), 2)
            print(str(temp) + " meters")
        else:
            meters = input("Enter meters: ")
            temp = round(metersToFeet(meters), 2)
            print(str(temp) + " feet")
        temp = input("Would you like to perform another conversion? (y/n): ")
        if temp == "n":
            going = False
            print("Thanks, bye!")


def title():
    print("Feet and Meters Converter")


def menu():
    ab = input("Conversions Menu:\na. Feet to Meters\nb. Meters to Feet \nSelect a conversion (a/b): ")
    if ab == "a" or ab == "A":
        return True
    elif ab == "b" or ab == "B":
        return False


main()
