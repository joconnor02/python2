intarray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    print("Here is the full list: " + str(intarray))
    print("Numbers every 2: " + str(intarray[1:-1:2]))
    print("Numbers every 3: " + str(intarray[2:-1:3]))
    print("Numbers every 4: " + str(intarray[3:-1:4]))


main()
