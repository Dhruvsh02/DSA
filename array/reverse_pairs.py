# hard problem 
# reverse pair problem : conditon : i<j and a[i] > 2 * a[j]
# brute force approach 

def reverse_pairs(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > 2 * arr[j]:
                count += 1
    return count

def main():
    arr = [40,25,19,12,9,6,2]
    result = reverse_pairs(arr)
    print(f"no of reverse pairs are: {result}")
if __name__ == "__main__":
    main()


# optimal approach using merge sort

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left +=1
    
    while right <= high:
        temp.append(arr[right])
        right +=1
    
    for i in range(len(temp)):
        arr[low + i] = temp[i]


def count_pairs(arr, low, mid, high):
    count = 0
    j = mid + 1
    for i in range(low, mid + 1):
        while j <= high and arr[i] > 2 * arr[j]:
            j += 1
        count += j - (mid + 1)
    return count


def merge_sort(arr, low, high):
    if low >= high:
        return 0
    mid = (low + high) // 2
    count = merge_sort(arr, low, mid)
    count += merge_sort(arr, mid + 1, high)
    count += count_pairs(arr, low, mid, high)
    merge(arr, low, mid, high)
    return count


def main():
    arr = [40, 25, 19, 12, 9, 6, 2]
    result = merge_sort(arr, 0, len(arr) - 1)
    print(f"Number of reverse pairs: {result}")
    print(f"Sorted array: {arr}")


if __name__ == "__main__":
    main()
