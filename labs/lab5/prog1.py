import numpy


def randQuicksort(S):
    if len(S) == 0:
        return S

    v = S[numpy.random.randint(0, len(S))]
    sL = [val for val in S if val < v]
    sV = [val for val in S if val == v]
    sR = [val for val in S if val > v]

    if len(sL) == 0 and len(sR) == 0:
        return S
    return randQuicksort(sL) + sV + randQuicksort(sR)


if __name__ == "__main__":
    n = int(input("n: "))  # s
    numArr = []
    for i in range(n):
        numArr.append(numpy.random.randint(0, n))

    print(randQuicksort(numArr))
