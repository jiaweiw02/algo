# Implement two separate programs that generate the n-th Fibonacci number. The
# programs should both take n as command line input. The first algorithm one should
# implement the recursive algorithm (fib1 on Page 3 of the textbook), and the second one
# should implement the iterative algorithm (fib2 on Page 4). You should measure the time
# it takes for each of these versions (use for example, the time it module in python) to
# calculate the n-th Fibonacci number for the following values of n: 1, 5, 10, 15, 20, 25,
# 30, 35, 40, 41, 42, 43. Finally, create a table of all your results and plot the time taken to
# compute the Fibonacci numbers using fib1 and fib2, with n on the x-axis and time on the
# y-axis.

#iterative version

import time
import sys
sys.set_int_max_str_digits(0)

def fib1(n):
    lst = [0, 1]
    for i in range (2, n+1):
        lst.append(lst[i-1] + lst[i-2])
    return lst[n]

if __name__ == "__main__":
    n = int(input("Enter the value for n: "))
    before = time.time()
    print(fib1(n))
    print("time: {}".format(time.time() - before))