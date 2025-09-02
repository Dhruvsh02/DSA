# count inversion in an array 
# means no. of pairs 
# brute force approach 

def count_inversion(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j] and i<j:
                count +=1

    return count
def main():
    arr = [5,3,2,4,1]
    result = count_inversion(arr)
    print(f"the no of count inversion is : {result}")
if __name__ == "__main__":
    main()

# optimal approach using merge sort

def ms(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    count = 0

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            count += (mid - left + 1)  # Inversions
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy sorted elements back to original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]

    return count

def merge_sort(arr, low, high):
    if low >= high:
        return 0

    mid = (low + high) // 2
    count = 0
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid + 1, high)
    count += ms(arr, low, mid, high)

    return count

def main():
    arr = [12, 11, 13, 5, 6, 7]
    result = merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
    print("Count of inversions:", result)

if __name__ == "__main__":
    main()
