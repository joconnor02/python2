import csv


def main():
    data = initCustList(open("customers.csv", "r"))
    print("Customer Viewer\n")
    while True:
        id = input("Enter Customer ID: ")
        print("")
        exists = False
        for cust in data:
            if cust.id == id:
                print(cust.nameaddress())
                exists = True
                break
        if not exists: {print("No customer with that ID.")}
        print()
        going = input("Continue? (y/n): ")
        if going.lower() == "n":
            break

def initCustList(file):
    f = csv.reader(file)
    skipline = True
    cust_list = []
    for line in f:
        if skipline:
            skipline = False
            continue
        cust = Customer(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        cust_list.append(cust)
    return cust_list


class Customer:
    def __init__(self, idnum, firstName, lastName, company, address, city, state, zip):
        self.id = idnum
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def nameaddress(self):
        if self.company == "":
            return self.firstName + " " + self.lastName + "\n" + \
               self.address + "\n" + \
               self.city + ", " + \
               self.state + " " + self.zip
        return self.firstName + " " + self.lastName + "\n" + \
               self.company + "\n" + \
               self.address + "\n" + \
               self.city + ", " + \
               self.state + " " + self.zip


main()
