def main():
    contacts = [["Max Bruhwin", "mbruhwin@msc.net", "6271236456"],
                ["Marc Morale", "mmorale@email.org", "7814678256"]]
    print("Contact Manager\n"
          "COMMAND MENU\n"
          "list - Display all contacts\n"
          "view - View a contact\n"
          "add - Add a contact\n"
          "del - Delete a contact\n"
          "exit - Exit program")
    while(True):
        inp = input("Command: ")
        match inp:
            case "list":
                num = 0
                for contact in contacts:
                    print(str(num) + ". " + contact[0])
                    num = num + 1
                num = 0
            case "view":
                num = input("Number: ")
                contact = contacts[int(num)]
                print("Name: " + contact[0] + "\n" +
                      "Email: " + contact[1] + "\n"
                      "Phone: " + contact[2])
            case "add":
                name = input("Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                contacts.append([name, email, phone])
            case "del":
                num = int(input("Number: "))
                name = contacts[int(num)][0]
                contacts.pop(num)
                print(name + " was deleted.")
            case "exit":
                break
    print("Bye!")


main()

