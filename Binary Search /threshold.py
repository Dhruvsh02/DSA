# find the smallest divisor given a threshold 
from math import ceil
def minDivisor(nums, threshold):
    for d in range(1,max(nums)+1):
        sum = 0
        for i in range(len(nums)):
            sum += ceil(nums[i]/d)
        if sum <= threshold:
            return d
    return -1   

def main():
    nums = [1,2,5,9]
    threshold = 6
    print(minDivisor(nums, threshold))
if __name__ == "__main__":
    main()

# binary search approach to find the minimum divisor
def minDivisor(nums, threshold):
    low,high= 1, max(nums)
    ans=-1
    while low < high:
        mid = (low+high)//2
        sum = 0
        for i in range(len(nums)):
            sum += ceil(nums[i]/mid)
        if sum <= threshold:
            ans = mid 
            high = mid-1
        else:
            low = mid + 1
    return ans
def main():
    nums = [1,2,5,9]
    threshold = 6
    print(minDivisor(nums, threshold))
if __name__ == "__main__":
    main()