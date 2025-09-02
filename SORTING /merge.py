def ms(arr,low,high,mid):
    temp = []
    left=low
    right=mid+1
   
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
            right +=1
    while (left<=mid):
        temp.append(arr[left])
        left +=1    
    while (right <=high):
        temp.append(arr[high])
        right +=1
    for i in range(len(temp)):
        arr[i + low] = temp[i]

def merge(arr,low,high):
    if (low >= high):
        return
    mid = (low + high) // 2
    merge(arr,low,mid)
    merge(arr,mid+1,high)
    ms(arr,low,mid,high)

def main():
    arr = [12, 11, 13, 5, 6, 7]
    merge(arr,0,len(arr) - 1)
    print("Sorted array is:", arr)
if __name__ == "__main__":
        main()
