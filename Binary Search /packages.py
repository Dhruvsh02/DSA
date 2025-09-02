# least capacity to ship the packages within D days

# brute force approach 

def daysrequired(wt,cap):
    day = 1
    load = 0
    for i in range(len(wt)):
        if load + wt[i] > cap:
            day = day+1
            load = wt[i]
        else:
            load += wt[i]
    return day
def leastCapacity(wt, D):
    for cap in range(max(wt), sum(wt)+1):
        if daysrequired(wt, cap) <= D:
            return cap
    return -1
def main():
    wt = [1,2,3,4,5,6,7,8,9,10]
    D = 5
    print(leastCapacity(wt, D))
if __name__ == "__main__":
    main()



# binary search approach to find the least capacity
def daysrequired(wt,cap):
    day = 1
    load = 0
    for i in range(len(wt)):
        if load + wt[i] > cap:
            day = day+1
            load = wt[i]
        else:
            load += wt[i]
    return day

def leastCapacity(wt, D):
    low,high = max(wt),sum(wt)
    ans = -1
    while low<= high:
        mid=(low+high)//2
        if daysrequired(wt,mid) <= D:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans  
def main():
    wt = [1,2,3,4,5,6,7,8,9,10]
    D = 5
    print(leastCapacity(wt, D))
if __name__ == "__main__":
    main()