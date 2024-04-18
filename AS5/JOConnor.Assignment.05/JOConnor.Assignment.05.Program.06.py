def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("\nHere it is:\ngcd(" + str(a) + "," + str(b) + ") = " + str(gcd(a,b)[0]) +
          "\ns(" + str(a) + "," + str(b) + ") = " + str(gcd(a,b)[1]) +
          "\nt(" + str(a) + "," + str(b) + ") = " + str(gcd(a,b)[2]))


def gcd(a, b):
    r1, r2, t1, t2, s1, s2 = a, b, 0, 1, 1, 0
    while r1 != 0:
        q, r1, r2 = r2//r1, r2%r1, r1
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2
    return r2, t1, s1


main()
