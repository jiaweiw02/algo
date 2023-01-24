import math
import random
import time

from prog1 import method1
from prog2 import method2


def method3(x, y):
    n = max(len(x), len(y))
    if n == 1:
        return method1(int(x), int(y))

    x_l, x_r = x[:math.ceil(len(x) >> 1)], x[math.ceil(len(x) >> 1):]
    y_l, y_r = y[:math.ceil(len(y) >> 1)], y[math.ceil(len(y) >> 1):]

    P1 = method3(x_l, y_l)
    P2 = method3(x_r, y_r)

    lhs_method3 = int(x_l, 2) + int(x_r, 2)
    lhs_method3 = str(lhs_method3)
    rhs_method3 = int(y_l, 2) + int(y_r, 2)
    rhs_method3 = str(rhs_method3)
    P3 = method3(lhs_method3, rhs_method3)
    return (P1 << n) + ((P3 - P2 - P1) << int(n / 2)) + P2


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
        bin_x = (bin(x))[2:]
        bin_y = (bin(y))[2:]
        Tbefore3 = time.time()
        print(bin_x, bin_y)
        method3(bin_x, bin_y)
        method3_lst.append(time.time() - Tbefore3)

    print("Average for method1: {}s".format(sum(method1_lst) / len(method1_lst)))
    print("Average for method2: {}s".format(sum(method2_lst) / len(method2_lst)))
    print("Average for method3: {}s".format(sum(method3_lst) / len(method3_lst)))

    # bin1 = input("Enter the first binary number: ")
    # bin2 = input("Enter the second binary number: ")
    # ans = method3(bin1, bin2)
    # print("Your answer in decimal is {}".format(ans))