# left rotate an array by one place 

def rotate(n,arr):
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

def main():
    arr = [1,2,3,4,5]
    n = len(arr)
    print("Before rotation: ",arr)
    arr = rotate(n,arr)
    print("After rotation: ",arr)
if __name__ == "__main__":
    main()

# left rotate an array by d places ( brute force approach )
# t c omplexity = O(n+d) and s c omplexity = O(n)
def left_rotate(arr, d):
    temp = arr[:d]     # list slicing
    # store the first d elements in a temporary array
    # rotate the array
    for i in range(d, len(arr)):
        arr[i - d] = arr[i]
    for i in range(len(arr) - d, len(arr)):
        arr[i] = temp[i - (len(arr) - d)]
    return arr
def main():
    arr = [1, 2, 3, 4, 5]
    d = 2
    print("Before rotation: ", arr)
    arr = left_rotate(arr, d)
    print("After rotation: ", arr)
if __name__ == "__main__":
    main()


# left rotate an array by d places ( efficient approach ) optimal 
# t c omplexity = O(n) and s c omplexity = O(1)

def rotate(arr,n,d):
    # reverse the first d elements
    reverse(arr, 0, d - 1)
    # reverse the remaining n-d elements
    reverse(arr, d, n - 1)
    # reverse the whole array
    reverse(arr, 0, n - 1)
    return arr
def reverse(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def main():
    arr = [1, 2, 3, 4, 5]
    d = 2
    n = len(arr)
    print("Before rotation: ", arr)
    arr = rotate(arr, n, d)
    print("After rotation: ", arr)
if __name__ == "__main__":
    main()