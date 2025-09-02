# count subarray sum equals k 

# brute force approach
def count_subarray_sum(arr, k):
    count = 0 
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for x in range(i,j+1):
                sum = sum + arr[x]
            if sum == k:
                count += 1
    return count

def main():
    arr = [1, 2, 3, 4, 5]
    k = 5
    result = count_subarray_sum(arr, k)
    print(f"Count of subarrays with sum {k}: {result}")
if __name__ == "__main__":
    main()



# better approach 
def count_subarray_sum_better(arr, k):
    count = 0 
    n = len(arr)
    for i in range(n):
        sum = 0 
        for j in range(i,n):
            sum += arr[j]
            if sum == k:
                count += 1
    return count    

def main():
    arr = [1, 2, 3, 4, 5]
    k = 5
    result = count_subarray_sum_better(arr, k)
    print(f"Count of subarrays with sum {k}: {result}")
if __name__ == "__main__":
    main()


# optimal approach using hashmap and prefix sum
def count_subarray_sum_hashmap(arr, k):
    count = 0
    n = len(arr)
    prefix_sum = 0
    sum_map = {0:1}
    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum - k in sum_map:
            count += sum_map[prefix_sum - k]
        if prefix_sum in sum_map:
            sum_map[prefix_sum] += 1
        else:
            sum_map[prefix_sum] = 1
    return count    

def main():
    arr = [1,2,3,-3,1,1,1,4,2,-3]
    k = 3
    result = count_subarray_sum_hashmap(arr,k)
    print(f"Count of subarrays with sum {k}: {result}")
if __name__ == "__main__":
    main()
