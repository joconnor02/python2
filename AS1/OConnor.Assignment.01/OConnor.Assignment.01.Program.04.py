from as01part4module import calcSalesTax, calcTotalAfterTax


def main():
    print("Sales Tax Calculator")
    going = True
    while going:
        pretax = count()
        print("Total: " + str(pretax))
        print("Sales Tax: " + str(calcSalesTax(pretax)))
        print("Total After Tax: " + str(calcTotalAfterTax(pretax)))
        temp = input("Again? (y/n): ")
        if temp == "n":
            going = False
    print("Thanks, bye!")


def count():
    print("ENTER ITEMS (ENTER 0 TO END)")
    going = True
    bank = 0
    while going:
        temp = input("Cost of item: ")
        bank = bank + float(temp)
        if temp == "0":
            going = False
    return bank


main()
