import math
import random
import time

from prog1 import method1
from prog2 import method2


def method3(x, y):
    n = max(len(bin(x)[2:]), len(bin(y)[2:]))
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x
    if n <= 1:
        return method1(x, y)

    # binX = bin(x)[2:]
    # binY = bin(y)[2:]

    x_l, x_r = x >> ((n >> 1)), x & ((1 << (n >> 1)) - 1)
    y_l, y_r = y >> ((n >> 1)), y & ((1 << (n >> 1)) - 1)

    # print("binx", binX, "x_l", x_l, "x_r", x_r)
    # print("biny", binY, "y_l", y_l, "y_r", y_r)

    P1 = method3(x_l, y_l)
    P2 = method3(x_r, y_r)
    P3 = method3(x_l + x_r, y_l + y_r)
    return (P1 << ((n >> 1) << 1)) + ((P3 - P1 - P2) << (n >> 1)) + P2


if __name__ == "__main__":
    d = int(input("Enter the number of digits: "))
    r = 10

    method1_lst = []
    method2_lst = []
    method3_lst = []

    for i in range(10):
        x = random.randint(10**(d-1), 10**d)
        y = random.randint(10**(d-1), 10**d)
        # time for method1
        Tbefore1 = time.time()
        method1(x, y)
        method1_lst.append(time.time() - Tbefore1)
        # time for method2
        Tbefore2 = time.time()
        method2(x, y)
        method2_lst.append(time.time() - Tbefore2)
        # time for method3
        Tbefore3 = time.time()
        method3(x, y)
        method3_lst.append(time.time() - Tbefore3)

    print("Average for method1: {}s".format(sum(method1_lst) / len(method1_lst)))
    print("Average for method2: {}s".format(sum(method2_lst) / len(method2_lst)))
    print("Average for method3: {}s".format(sum(method3_lst) / len(method3_lst)))