# move all zeros to the end of the array( brute force approach)

def zero(arr, n):
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
    
    nz = len(temp)
    
    # Copy non-zero elements back
    for i in range(nz):
        arr[i] = temp[i]
    
    # Fill remaining with zeros
    for i in range(nz, n):
        arr[i] = 0

    return arr

def main():
    arr = [1, 2, 0, 0, 4, 5, 0, 6, 2, 0]
    n = len(arr)
    arr = zero(arr, n)
    print("new array", arr)

if __name__ == "__main__":
    main()


# move all zeros to the end of the array( efficient approach)
# t c omplexity = O(n) and s c omplexity = O(1)

def move_zero(arr, n):
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    if j ==1:
        return arr
    for i in range(j+1, n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr

def main():
    arr = [1, 2, 0, 0, 4, 5, 0, 6, 2, 0]
    n = len(arr)
    arr = move_zero(arr, n)
    print("current array", arr)
if __name__ == "__main__":
    main()
        