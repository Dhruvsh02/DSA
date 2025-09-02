# largest subarray with sum 0

def largest_subarray_sum_0(arr):
    n = len(arr)
    maxi = 0 
    sum = 0
    sum_map = {0: -1}
    for i in range(n):
        sum += arr[i]
        if sum in sum_map:
             maxi = max(maxi, i - sum_map[sum])
        else:
             sum_map[sum] = i
    return maxi 

def main(): 
    arr = [1, -1, 3, 2, -2, -3, 3]
    result = largest_subarray_sum_0(arr)
    print(f"Largest subarray with sum 0 has length: {result}")
if __name__ == "__main__":
    main()
