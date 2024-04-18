def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    while True:
        if inSet:
            print("Yes, " + str(a) + " is in Z" + str(b))
        else:
            print(str(a) + " is not in Z" + str(b))
            break;
        if hasInverse(a,b):
            print("gcd(" + str(a) + "," + str(b) + ") = " + str(gcd(a,b)[0]) + "\nThere is a multiplicative inverse for " + str(a) + " which is t = " + str(gcd(a,b)[1]))
            break;
        else:
            print("gcd(" + str(a) + "," + str(b) + ") = " + str(gcd(a,b)[0]) + "\nThere is NO multiplicative inverse.")
            break;



def inSet(a,b):
    setb = []
    for i in range(b):
        if a == i:
            return True
    return False


def hasInverse(a,b):
    if gcd(a,b)[0] == 1:
        return True
    return False


def gcd(a, b):
    r1, r2, t1, t2, s1, s2 = a, b, 0, 1, 1, 0
    while r1 != 0:
        q, r1, r2 = r2//r1, r2%r1, r1
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2
    return r2, t1, s1


main()
