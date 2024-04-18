
def main():
    oglist = [19, 65, 57, 39, 45, 152, 639, 121, 44, 90, 190, 200, 26, 130]
    finalist = list(filter(lambda i: i % 13 == 0 or i % 15 == 0, oglist))
    print("Original List:\n" + str(oglist) + "\nNumbers from the list above divisible by 13 or 15:\n" + str(finalist))


main()
