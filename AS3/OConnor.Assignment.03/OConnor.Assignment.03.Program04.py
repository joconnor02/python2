provided = [(14, 12), (24, 73, 59), (43, 4), (23, 33, 94, 12)]


def main():
    print("Original list of tuplies: \n" + str(provided))
    print("Convert to a list of lists: \n" + str(lol()))


def lol():
    z = []
    for x in provided:
        y = sorted(x)
        z.append(y)
    return z


main()
