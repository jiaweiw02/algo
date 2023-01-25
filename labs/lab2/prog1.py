def method1(x, y):
    yBin = str(bin(y))
    shift = 0
    result = 0

    for num in reversed(yBin):
        if num == '1':
            line = x << shift
            result += line
        shift += 1
    
    return result


if __name__ == "__main__":
    print(method1(6, 6))
