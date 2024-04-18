def main():
    print("Customer/Employee Data Entry\n")
    while True:
        inpc = input("Customer or Employee? (c/e): ")
        if not (inpc.lower() == "c" or inpc.lower() == "e"):
            continue
        print("\nDATA ENTRY")
        inpfn = input("First name:")
        inpln = input("Last name: ")
        inpem = input("Email: ")
        if inpc.lower() == "c":
            inpnum = input("Number: ")
            cust = Customer(inpfn, inpln, inpem, inpnum)
            print("\nCUSTOMER")
            print("Name: " + cust.firstname + " " + cust.lastname)
            print("Email: " + cust.email)
            print("Number: " + cust.number)

        else:
            inpssn = input("SSN: ")
            emp = Employee(inpfn, inpln, inpem, inpssn)
            print("\nEMPLOYEE")
            print("Name: " + emp.firstname + " " + emp.lastname)
            print("Email: " + emp.email)
            print("Number: " + emp.ssn)
        going = input("Continue? (y/n): ")
        if going == "y":
            continue
        else:
            break
    print("\nBye!")


class Person:
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


class Customer(Person):
    def __init__(self, firstname, lastname, email, number):
        self.number = number
        super().__init__(firstname, lastname, email)


class Employee(Person):
    def __init__(self, firstname, lastname, email, ssn):
        self.ssn = ssn
        super().__init__(firstname, lastname, email)


main()
