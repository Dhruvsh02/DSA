# finding the sum of the maximum subarray (better approach) t.c O(n^2)

def subarry_sum(arr):
    n = len(arr)
    maxi= -1
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            maxi = max(maxi,sum)
    return maxi
def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    result = subarry_sum(arr)
    print("The maximum subarray sum is: ", result)
if __name__ == "__main__":
    main()

# using kadane's algorithm
# This algorithm is used to find the maximum subarray sum in O(n) time complexity
# It is an optimal solution for the maximum subarray sum problem

def subarry_sum(arr):
    n = len(arr)
    #ans_start = -1    used for storing the starting index of the maximum subarray
    #ans_end = -1     used for storing the ending index of the maximum subarray
    maxi = -1
    sum=0
    start = 0
    for i in range(n):
        if sum ==0:        # if sum is 0 then start from the current index
            start = i      # used for storing the starting index of the current subarray
        sum = sum+arr[i]
        if sum > maxi:
            maxi = sum
            ans_start = start   # used for printing the maximum subarray
            ans_end = i         # used for printing the maximum subarray
        if sum <  0:
            sum = 0
    #print("The maximum subarray is: ", arr[ans_start:ans_end+1])
    return maxi
def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    result = subarry_sum(arr)
    print("The maximum subarray sum is: ", result)
if __name__ == "__main__":
    main()


