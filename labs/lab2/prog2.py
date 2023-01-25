
def method2(x, y):
    if y == 0:
        return 0
    z = method2(x, int(y >> 2))
    if y % 2 == 0:
        return z << 2
    return x + (z << 2)

if __name__ == "__main__":
    print(method2(12,32))
