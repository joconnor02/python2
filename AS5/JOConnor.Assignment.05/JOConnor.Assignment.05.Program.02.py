
def main():
    letterset = {'b', 'D', 'o', 'g', 'U', 'a', 'i'}
    dupeset = str(list(map(dupe, letterset)))
    print("Original Characters:\n" + str(letterset) + "\nAfter converting above characters to upper and lowercase and removing duplicate characters\n" + dupeset)


def dupe(letter):
    return letter.upper(), letter.lower()


main()
