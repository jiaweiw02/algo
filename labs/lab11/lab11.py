def cover(S, n):
    remaining = set(range(1, n + 1))

    while len(remaining) > 0:
        high = max(S, key=lambda it: len(remaining & it))
        print(high)
        remaining -= high


if __name__ == "__main__":
    n = 11
    S = [
        {1, 3, 5, 7, 10, 11},
        {1, 2, 4, 5, 11},
        {4, 8, 9},
        {1, 3, 5, 8, 9, 10},
        {2, 6, 10}
    ]

    cover(S, n)
