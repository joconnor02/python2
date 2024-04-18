def main():
    inputf = input("Enter the Input File: ")
    outputf = input("Enter the Output File: ")
    action(inputf, outputf)


def action(inputf, outputf):
    inobj = open(inputf, "r")
    outobj = open(outputf, "w")
    data = inobj.read()
    outobj.write(data)
    print(data)


main()
