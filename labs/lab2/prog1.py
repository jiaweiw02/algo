import math


def method1(a, b):
    if a == 0 or b == 0:
        return 0
    str_a = bin(a)
    shift = int(math.log2(b))
    b -= pow(2, shift)
    str_a += "0" * shift
    rem_value = 0
    for i in range(b):
        rem_value += a
    return int(str_a, 2) + rem_value


if __name__ == "__main__":
    print(method1(55, 6))
