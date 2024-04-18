def main():
    going = True
    while(going):
        first = input("Enter the first String: ")
        second = input("Enter the second String: ")
        print("Original Strings: " + first + ", " + second)
        end = commonend(first, second)
        print("Common ending between the two strings: " + end)
        go = input("Try again? (y/n)")
        if go == "n":
            going = False
    print("Bye!")


def commonend(one, two):
    common = ""
    if len(one) < len(two):
        length = len(one)
    else:
        length = len(two)
    for i in range(length):
        if i == 0:
            continue
        if one[-i] == two[-i]:
            common = common + one[-i]
    if one[-length] == two[-length]:
            common = common + one[-length]
    reverse = common[slice(-1, -length - 1, -1)]
    return reverse


main()
