def main():
    print("Even or Odd Checker")
    temp = input("Enter an integer: ")
    if isEven(temp):
        print("This is an even number.")
    else:
        print("This is an odd number.")


def isEven(num):
    if int(num) % 2 == 0:
        return True
    return False


main()
