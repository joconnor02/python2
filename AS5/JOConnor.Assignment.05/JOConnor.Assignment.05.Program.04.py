midtermgrades = [90, 76, 94]
finalsgrades = [78, 79, 90]
studentlist = ['Marie', 'Michael', 'Marge']


def main():
    inBook = zip(studentlist, midtermgrades, finalsgrades)
    gradebook = []
    for students in inBook:
        student = list(students)
        if student[2] > student[1]:
            student.pop(1)
        else:
            student.pop(2)
        gradebook += student
    print("midterms: " + str(midtermgrades) + "\nfinals: " + str(finalsgrades) + "\nstudents: " + str(studentlist) + "\n" + str(gradebook))


main()


