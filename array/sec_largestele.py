# second largest and second smallest element in a array

import sys

def second_largest(arr,n):
    largest = arr[0]
    second_largest = -1
    
    for i in range(1,n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i]!= largest:
            second_largest = arr[i]
    if second_largest == -1:
        print("There is no second largest element")
    else:
        print("The second largest element is:", second_largest)
    return second_largest

def second_smallest(arr,n):
    smallest = arr[0]
    second_smallest = sys.maxsize
    for i in range(1,n):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] < second_smallest and arr[i]!= smallest:
            second_smallest = arr[i]
    
    if second_smallest == sys.maxsize:
        print("There is no second smallest element")
    else:
        print("The second smallest element is:", second_smallest)
    return second_smallest

def main():
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    second_largest(arr,n)
    second_smallest(arr,n)
if __name__ == "__main__":
    main()


