# minimum in rotated sorted array 

def minimum_in_rotated_sorted_array(arr):
    low , high = 0 , len(arr) - 1
    ans = -1
    while low < high:
        mid = (low+high)//2
        # Check if the array is already sorted
        # then always arr[low] will be the minimum in that search space 
        if arr[low] <= arr[high]:
            ans = min(ans,arr[low])
            break
        if arr[low] <= arr[mid]:
            ans = min(ans,arr[low]) 
            low = mid + 1
        else:
            ans = min(ans,arr[mid])
            high = mid - 1
        return ans if ans != -1 else arr[low]
    
def main():
    arr = [4,5,6,7,0,1,2]
    print(minimum_in_rotated_sorted_array(arr)) 
if __name__ == "__main__":
    main()

