
def main():
    oglist = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:\n" + str(oglist) + "\nTriple list of said numbers:\n" + str(list(map(triple, oglist))))


def triple(num):
    return num * 3


main()
