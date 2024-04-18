def main():
    print("Prime Number Checker")
    going = True
    while going:
        temp = getInput()
        if temp == 0:
            print("Invalid integer. Please try again.")
            continue
        else:
            if numFactors(temp) == 2:
                print(str(temp) + " is a prime number.")
            else:
                print(str(temp) + " is NOT a prime number")
                print("It has " + str(numFactors(temp)) + " factors.")
        temp2 = input("Try again? (y/n): ")
        if temp2 == "n":
            going = False
    print("Bye!")


def getInput():
    temp = int(input("Please enter an integer between 1 and 5000: "))
    if temp > 1 and temp < 5000:
        return temp
    return 0


def numFactors(num):
    count = 0
    for i in range (1, num + 1):
        if num % i == 0:
            count = count + 1
    return count


main()
