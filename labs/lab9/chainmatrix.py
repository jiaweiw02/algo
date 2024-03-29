def chainmatrix(D):
    n = len(D)
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]

    for d in range(1, n - 1):
        for i in range(1, n - d):
            j = i + d
            s_min = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + D[i - 1] * D[k] * D[j]
                if q < s_min:
                    s_min = q
                    s[i][j] = k
            m[i][j] = s_min
    print(m[1][n - 1])

    for it in s:
        print(it)


if __name__ == "__main__":
    D = [5,4,6,2,7]
    chainmatrix(D)
