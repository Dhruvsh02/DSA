# search in a roated sorted array for unique elements
# in this our first apporach is linear search using O(n) time complexity which is not efficient
# we will use binary search to find the element in O(log n) time complexity

def search_in_rotated_array(arr, target):
    low , high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return mid
        # check if left side is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid -1
            else:
                low = mid + 1
        # check if right side is sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

def main():
    arr = [7,8,9,1,2,3,4,5,6]
    target = 1
    result = search_in_rotated_array(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array")
if __name__ == "__main__":
    main()



# search in rotated sorted array for duplicate elements
# in this our first apporach is linear search using O(n) time complexity which is not efficient
# we will use binary search to find the element in O(log n) time complexity

def search_in_rotated_array(arr, target):
    low , high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return True
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low +=1
            high -=1
            continue
        # check if left side is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid -1
            else:
                low = mid + 1
        # check if right side is sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False    
def main():
    arr = [7,8,9,1,2,3,3,3,4,5,6]
    target = 3
    result = search_in_rotated_array(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array")
if __name__ == "__main__":
    main()