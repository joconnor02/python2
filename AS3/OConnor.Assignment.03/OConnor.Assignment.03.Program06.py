def main():
    sort("red Green black White Pink")
    print("")
    sort("I am enjoying my Cybersecurity courses at RWU so much")


def sort(inp):
    print("Original Word:\n\"" + inp + "\"\nSorted Word Based On Its First Character:")
    work = list(inp.split(" "))
    work.sort(key=str.casefold)
    out = ""
    for s in work:
        out += s
        out += " "
    print("\"" + out + "\"")


main()
