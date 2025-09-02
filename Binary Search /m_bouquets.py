# minimum number of days to make M bouquets from flowers
# brute force approach 

def possible(arr,day,m,k):
    count = 0
    bouquets = 0
    for i in range(len(arr)):
        if arr[i] <= day:
            count += 1
        else:
            bouquets += count // k
            count = 0
    bouquets += count // k
    if bouquets >= m:
        return True
    return False
def minDays(arr, m, k):
    if len(arr) < m * k:
        return -1
    for i in range(min(arr),max(arr)):
        if possible(arr, i, m, k) == True:
            return i
    return -1

def main():
    arr = [7,7,7,7,13,12,11,7]
    m = 2
    k = 3
    print(minDays(arr, m, k))
if __name__ == "__main__":
    main()


# now will use binary search to find the minimum number of days

def possible(arr,day,m,k):
    count = 0
    bouquets = 0
    for i in range(len(arr)):
        if arr[i] <= day:
            count += 1
        else:
            bouquets += count // k
            count = 0
    bouquets += count // k
    if bouquets >= m:
        return True
    return False
def minDays(arr, m, k):
    if len(arr) < m*k:
        return -1
    left ,right = min(arr), max(arr)
    ans = -1
    while left <= right:
        mid = (left + right)//2
        if possible(arr,mid,m,k) == True:
            ans = mid
            right = mid-1
        else:
            left = mid + 1
    return ans
def main():
    arr = [7,7,7,7,13,12,11,7]
    m = 2
    k = 3
    print(minDays(arr, m, k))
if __name__ == "__main__":
    main()