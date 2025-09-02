# number of subarray with xor k 

# brute force approach and better approach

def subarray_xor_k(arr, k):
    n = len(arr)
    count = 0 
    for i in range(n):
        XOR = 0 
        for j in range(i, n):
            XOR = XOR ^ arr[j]
            if XOR == k:
                count += 1 
    return count 

def main():
    arr = [4,2,2,6,4]
    k = 6
    result = subarray_xor_k(arr, k)
    print(f"Count of subarrays with XOR = {k}: {result}")

if __name__ == "__main__":
    main()


# optimal approach using hashmap
def subarray_xor_k_optimal(arr, k):
    n = len(arr)
    count = 0
    xor_map = {0: 1}  # Initialize with XOR 0 having one occurrence
    current_xor = 0
    for i in range(n):
        current_xor ^= arr[i]
        x = current_xor ^ k
        count += xor_map.get(x, 0)  # Get the count of previous XORs that match 
        xor_map[current_xor] = xor_map.get(current_xor, 0) + 1
    return count

def main_optimal():
    arr = [4, 2, 2, 6, 4]
    k = 6
    result = subarray_xor_k_optimal(arr, k)
    print(f"Count of subarrays with XOR = {k} (optimal): {result}")
if __name__ == "__main__":
    main_optimal()