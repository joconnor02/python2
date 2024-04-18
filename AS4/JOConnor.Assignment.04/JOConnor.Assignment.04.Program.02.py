import random


def main():
    print("Random Integer List\n")
    while True:
        try:
            size = int(input("How many random integers should the list contain?: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        break
    while True:
        int_list = RandomIntList(size)
        print("\nRandom Integers\n===============")
        print("Integers: " + int_list.__str__())
        print("Count: " + str(int_list.size))
        print("Total: " + str(int_list.sum()))
        print("Average: " + str(int_list.avg()))
        going = input("\nContinue? (y/n): ")
        if going.lower() == "n":
            break
    print("Bye!")


class RandomIntList(list):

    def __init__(self, size):
        self.size = size
        for i in range(size):
            self.append(random.randint(1, 100))

    def sum(self):
        count = 0
        for num in self:
            count += num
        return count

    def avg(self):
        return round(sum(self) / self.size, 2)

    def __str__(self):
        return ", ".join(map(str, self))


main()
