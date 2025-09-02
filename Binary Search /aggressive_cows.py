# addressive cows : min distance between cows is maximum 
# linear approach 

def can_we_place(arr,distance,cows):
    cow_count = 1
    last = arr[0]
    for i in range(1,len(arr)):
        if arr[i] - last >= distance:
            cow_count+=1
            last= arr[i]
    if cow_count >= cows:
        return True
    else:
        False



def aggressive_cows(arr,cows):
    arr.sort()
    for i in range(1,max(arr)-min(arr)):
        if can_we_place(arr,i,cows) == True:
            continue
        else:
            return i-1
        
def main():
    arr=[0,3,4,7,10,9]
    cows = 4
    result = aggressive_cows(arr,cows)
    print(f"the min distance between cows is max:  {result}")
if __name__ == "__main__":
    main()

# binary search approach 
 
def can_we_place(arr,distance,cows):
    cow_count = 1
    last = arr[0]
    for i in range(1,len(arr)):
        if arr[i] - last >= distance:
            cow_count+=1
            last= arr[i]
    if cow_count >= cows:
        return True
    else:
        False
def aggressive_cows(arr,cows):
    arr.sort()
    low , high = 1 , max(arr)
    while low <= high :
        mid = (low+high)//2
        if can_we_place(arr,mid,cows) == True:
            low = mid+1
        else:
            high = mid-1
    return high 
def main():
    arr=[0,3,4,7,10,9]
    cows = 4
    result = aggressive_cows(arr,cows)
    print(f"the min distance between cows is max:  {result}")
if __name__ == "__main__":
    main()
