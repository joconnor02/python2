def main():
    providedList = [('red', 'green'), ('pink', 'black'), ('orange', 'blue')]
    print("Original List of tuples:\n" + str(providedList) + "\n\nConvert to a list of strings: ")
    print(list(map(" ".join, providedList)))


main()

