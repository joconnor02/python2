ages = {'Chris': 18, 'Nicole': 32, 'Doug': 22, 'Betty': 45, 'David': 33, 'Lilah': 20}


def main():
    print("Original dictionary elements: \n" + str(ages) + "\n")
    print("Maximum Age is for " + str(max(ages, key=ages.get)) + " which is " + str(ages.get(max(ages, key=ages.get))))
    print("Minimum Age is for " + str(min(ages, key=ages.get)) + " which is " + str(ages.get(min(ages, key=ages.get))))


main()
