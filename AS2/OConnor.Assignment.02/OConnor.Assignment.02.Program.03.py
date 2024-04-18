def main():
    going = True
    while(going):
        num = int(input("Enter a Digit: "))
        print("Original Number: " + str(num))
        print("Largest Digit of the said number: " + str(largest(num)))
        print("Smallest Digit of the said number: " + str(smallest(num)))
        go = input("Try another number? (y/n) ")
        if go == "n":
            going = False
    print("Bye!")

def largest(num):
    largest = 0
    while num > 0:
        last = num % 10
        if last > largest:
            largest = last
        num = num // 10
    return largest


def smallest(num):
    smallest = num % 10
    while num > 0:
        last = num % 10
        if last < smallest:
            smallest = last
        num = num // 10
    return smallest


main()
