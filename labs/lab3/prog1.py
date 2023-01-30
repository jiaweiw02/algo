
# program 1

import math

def modexp(x, y, N):
    # input x, y, N
    # output x^y mod N
    if y == 0:
        return 1
    z = modexp(x, math.floor(y / 2), N)
    if y % 2 == 0:
        return (z ** 2) % N
    else:
        return (x * (z ** 2)) % N


if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    print(modexp(a,b,c))