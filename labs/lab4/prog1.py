import numpy

def selection(S, k):
    v = S[numpy.random.randint(0, len(S))]
    sL = [val for val in S if val < v]
    sV = [val for val in S if val == v]
    sR = [val for val in S if val > v]

    if k <= len(sL):
        return selection(sL, k)
    elif len(sL) < k and k <= (len(sL) + len(sV)):
        return v
    elif k > (len(sL) + len(sV)):
        return selection(sR, k - len(sL) - len(sV))

if __name__ == "__main__":
    n = int(input("n: ")) # s
    k = int(input("k: ")) # k

    if (k > n):
        print("Error: the value of k cannot be larger than n")
        exit()

    numArr = []
    for i in range(n):
        numArr.append(numpy.random.randint(0, n))
    
    print("select", selection(numArr, k))
    print("array", numArr)
    print()
    numArr.sort()
    print("sorted array", numArr)

