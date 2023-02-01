import random
from prog1 import modexp

# program 2
def primality2(N, k):
    s = set()
    for i in range(k):
        num = random.randint(1, N-1)
        # while num in s:
        #     num = random.randint(1, N-1)
        s.add(num)

    l = list(s)
    for each in l:
        if (modexp(each, N-1, N) != 1):
            return False
        # if (each ** (N-1)) % N != 1:
        #     return False
    
    return True


if __name__ == "__main__":
    carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841,
                    29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081,
                    188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881]
    success = 0
    failure = 0
    total = 0
    k = 1
    for a in carmichael:
        if (primality2(a, k)):
            print("{}\tis prime".format(a))
            failure += 1
        else:
            print("{}\tis not prime".format(a))
            success += 1
        total += 1

    print("Probability of failure is {} out of {}, or {}".format(failure, total, failure/total))
    