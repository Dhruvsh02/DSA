# remove duplicate in place of sorted array 

def remove_dup(arr,n):
    i = 0
    for j in range(1,n):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i += 1
    return i + 1
def main():
    arr = [1,2,3,4,2,3,1,1,2,3,4,4,4,5]
    n = len(arr)
    arr.sort()
    print("Sorted array:", arr)
    new_length = remove_dup(arr, n)
    print("Array after removing duplicates:", arr[:new_length])
    print("New length of array:", new_length)
if __name__ == "__main__":
    main()