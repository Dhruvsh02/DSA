import heapq 
# minimise maximum distance between gas stations 
# note -> answers within 10^-6 og the actual original answer will be accepted.
# brute force approach 

def gas_station(arr,k):
    n = len(arr)
    how_many = [0] * (n-1)
    for _ in range(k):
        maxsection = -1
        maxindex = -1
        for i in range(n-1):
            diff = arr[i+1] - arr[i]
            sectionlen = diff // (how_many[i] + 1)
            if sectionlen > maxsection :
                maxsection = sectionlen 
                maxindex = i
        how_many[maxindex] +=1
    maxans = -1
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        sectionlen = diff // (how_many[i] + 1)
        maxans = max(maxans , sectionlen)
    return maxans 

def main():
    arr = [1,13,17,23]
    k = 5
    result = gas_station(arr,k)
    print(f"the minimise maximum distance between gas stations is : {result}")
if __name__ == "__main__":
    main()


# better appraoch using priority queue : heapq 
#heapp is used for finding the min_heap so we will -ve the value to find max-heap

def gas_station(arr,k):
    n = len(arr)
    how_many = [0] * (n-1)
    pq = []
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        heapq.heappush(pq, (-diff,i))
    for _ in range(k):
        neg_len , sec_ind = heapq.heappop(pq)
        how_many[sec_ind] +=1
        inidiff = arr[sec_ind + 1] - arr[sec_ind]
        newsec_len = inidiff / (how_many[sec_ind] + 1)
        heapq.heappush(pq , (-newsec_len , sec_ind))
    return -pq[0][0]
    
def main():
    arr = [1,13,17,23]
    k = 5
    result = gas_station(arr,k)
    print(f"the minimise maximum distance between gas stations is : {result}")
if __name__ == "__main__":
    main()


# binary search approach : optimal approach 

def count_gas_station(arr,dist):
    cut = 0
    for i in range(len(arr)-1):
        gap = arr[i+1] - arr[i]
        cut += int(gap / dist)
    return cut
def gas_station(arr,k):
    n = len(arr)
    low,high = 0,0

    for i in range(n-1):
        high = max(high, (arr[i+1]- arr[i]))

    while high - low > 1e-6:
        mid = (low + high) / 2.0
        count = count_gas_station(arr,mid)
        if count > k:
            low = mid
        else:
            high = mid 
    return high 
def main():
    arr = [1,13,17,23]
    k = 5
    result = gas_station(arr,k)
    print(f"the minimise maximum distance between gas stations is : {result}")
if __name__ == "__main__":
    main()

