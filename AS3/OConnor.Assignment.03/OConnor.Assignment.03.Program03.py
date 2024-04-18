students = [
    {'Name': 'Doug', 'Age': 18},
    {'Name': 'Mathew', 'Age': 22},
    {'Name': 'Roxanne', 'Age': 20},
    {'Name': 'Jane', 'Age': 18}]


def main():
    print("Original list of dictionaries:\n" + str(students))
    print("Here are the values of the \"Name\" key: " + str(getValues("Name")))
    print("Here are the values of the \"Age\" key: " + str(getValues("Age")))


def getValues(key):
    temp = []
    for x in students:
        temp.append(x[key])
    return temp


main()
