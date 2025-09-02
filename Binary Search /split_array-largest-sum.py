# painters partition and split array : largest sum - min(max)

def partition(arr,painter):
    paint = 1
    parti = 0
    for i in range(len(arr)):
        if parti + arr[i] <= painter:
            parti += arr[i]
        else:
            paint += 1
            parti = arr[i]
    return paint 
def painters(arr,k):
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low+high)//2
        if partition(arr,mid) > k:
            low = mid+1
        else:
            high = mid-1
    return low
def main():
    arr = [10,20,30,40]
    k = 2
    result = painters(arr,k)
    print(f"painter's partition or split array-largest sum : {result}")
if __name__=="__main__":
    main()

