# merge sorted arrays without extra space 
# Brute force approach

def merge_sorted_arrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    arr3 = [0] * (n+m)
    left = 0
    right = 0
    index = 0
    while left < n and right < m:
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
            index += 1
        else:
            arr3[index] = arr2[right]
            right += 1
            index += 1
    while left < n:
        arr3[index] = arr1[left]
        left += 1
        index += 1
    while right < m:
        arr3[index] = arr2[right]
        right += 1
        index += 1
    for i in range(n+m):
        if i<n:
            arr1[i] = arr3[i]
        else:
            arr2[i-n] = arr3[i]

    return arr3 , arr1, arr2

def main():
    arr1 = [1, 3, 5, 8]
    arr2 = [2, 4, 6]
    result = merge_sorted_arrays(arr1, arr2)
    print(f"Merged array: {result}")
if __name__ == "__main__":
    main()

# better approach using 2 pointers
def merge_sorted_arrays_optimal(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    left = n-1
    right = 0
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break
    arr1.sort()
    arr2.sort()
    return arr1, arr2

def main():
    arr1 = [1, 3, 5, 8]
    arr2 = [2, 4, 6]
    result1, result2 = merge_sorted_arrays_optimal(arr1, arr2)
    print(f"Merged array 1: {result1}, Merged array 2: {result2}")
if __name__ == "__main__":
    main()

# optimal approach using gap method 

def merge_sorted_arrays_gap(arr1,arr2):
    n = len(arr1)
    m = len(arr2)   
    total = n + m
    gap = total // 2 + total % 2
    while gap > 0:
        left = 0 
        right = gap 
        while right < total:
            if left < n and right >= n:
                if arr1[left] > arr2[right - n]:
                    arr1[left], arr2[right - n] = arr2[right - n], arr1[left]
            elif left >= n and right < total:
                if arr2[left - n] > arr2[right - n]:
                     arr2[left - n], arr2[right - n] = arr2[right - n], arr2[left - n]
            else: 
                if arr1[left] > arr1[right]:
                    arr1[left], arr1[right] = arr1[right], arr1[left]
            left += 1
            right += 1
        if gap == 1:
            break 
        gap = gap // 2 + gap % 2

    return arr1, arr2

def main():
    arr1 = [1, 3, 5, 8]
    arr2 = [2, 4, 6]
    result1, result2 = merge_sorted_arrays_gap(arr1, arr2)
    print(f"Merged array 1: {result1}, Merged array 2: {result2}")
if __name__ == "__main__":  
    main()