def main():
    num = input("Enter a Positive Number: ")
    result = cubeless(int(num))
    print("Sum of cubes smaller than the specified number: " + str(result))


def cubeless(num):
    sum = 0
    for i in range(num):
        cube = i * i * i
        sum = sum + cube
        i = i - 1
    return sum


main()
