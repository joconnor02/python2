def main():
    print("Tip Calculator\nINPUT")
    while True:
        try:
            com = float(input("Cost of meal: "))
        except ValueError:
            print("Must be valid decimal number. Please try again.")
            continue
        if com <= 0:
            print("Must be greater than 0. Please try again.")
            continue
        else:
            com = round(com, 2)
            break
    while True:
        try:
            tip = int(input("Tip percent: "))
        except ValueError:
            print("Must be valid integer. Please try again.")
            continue
        if tip <= 0:
            print("Must be greater than 0. Please try again.")
            continue
        else:
            break
    tipamount = round(com * (tip / 100), 2)
    totalamount = round(tipamount + com, 2)
    print("OUTPUT"
          "\nCost of meal: " + str(com) +
          "\nTip percent: " + str(tip) +
          "% \nTip amount: " + str(tipamount) +
          "\nTotal amount: " + str(totalamount))


main()
