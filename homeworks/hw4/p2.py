

def sortArr(A):
    R = max(A) - min(A)
    count = [0 for i in range(R + 1)]

    for num in A:
        index = num - min(A)
        count[index] += 1
    
    sortedA = []
    for i in range(len(count)):
        value = i + min(A)
        
        for dup in range(count[i]):
            sortedA.append(value)
    
    return sortedA

if __name__ == "__main__":
    arr = [1, 8, 4, 2, 0, 5, 102, 5, 3]
    print(sortArr(arr))
