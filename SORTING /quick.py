def partition(arr,low,high):
    pivot = arr[low]
    i = low 
    j = high 
    while i < j:
        while arr[i] <= pivot and i <= high-1:
            i += 1
        while arr[j] > pivot and j >= low+1:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]   # swap pivot with arr[j]
    # pivot is now at j
    return j
def quicksort(arr,low,high):
    if low < high:
        pindex = partition(arr,low,high)
        quicksort(arr,low,pindex - 1)
        quicksort(arr,pindex + 1,high)
def main():
    arr = [12, 11, 13, 5, 6, 7]
    quicksort(arr,0,len(arr) - 1)
    print("Sorted array is:", arr)
if __name__ == "__main__":
        main()