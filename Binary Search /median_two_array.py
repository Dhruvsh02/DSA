# meadian of two sorted arrays 
# brute force solution 

def median(arr1,arr2):
    arr3 = []
    i ,j = 0,0
    n = len(arr1)
    m = len(arr2)
    while i < n and j < m :
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    while i < n:
        arr3.append(arr1[i])
        i+=1
    while j < m:
        arr3.append(arr2[j])
        j+=1
    k = n+m
    if k % 2 == 1:
        return arr3[k//2]
    
    return (arr3[k//2] + arr3[k//2-1]) / 2
    
def main():
    arr1 = [2,4,5,6]
    arr2 = [1,2,3,4]
    result = median(arr1,arr2)
    print(f"the median of two sorted array is : {result}")
if __name__=="__main__":
    main()

# better approach 

def median(arr1,arr2):
    arr3 = []
    i ,j = 0,0
    n = len(arr1)
    m = len(arr2)
    k = n+m
    ind1 = k//2
    ind2 = ind1-1
    count = 0
    el1 , el2 = -1 , -1
    while i < n and j < m :
        if arr1[i] < arr2[j]:
            if count == ind1:
                el1 = arr1[i]
            if count == ind2:
                el2 = arr1[i]
            count +=1
            i+=1            
        else:
            if count == ind1:
                el1 = arr2[j]
            if count == ind2:
                el2 = arr2[j]
            count +=1
            j+=1
    while i < n:
        if count == ind1:
            el1 == arr1[i]
        if count == ind2:
            el2 == arr1[i]
        count +=1
        i +=1
    while j < m:
        if count == ind1:
            el1 == arr2[j]
        if count == ind2:
            el2 == arr2[j]
        count +=1
        j +=1
    if k%2 == 1:
        return el2
    return (el1+el2)/2
def main():
    arr1 = [2,4,5,6]
    arr2 = [1,2,3,4]
    result = median(arr1,arr2)
    print(f"the median of two sorted array is : {result}")
if __name__=="__main__":
    main()



# optimal approach using binary search 

def median_sorted_array(arr1,arr2):
    n1= len(arr1)
    n2= len(arr2)
    if n1 > n2:
        return median_sorted_array(arr1,arr2)
    low ,high = 0,n1
    n = n1+n2
    left = (n1+n2+1)//2
    while low<=high:
        mid1=(low+high) >> 1
        mid2 = left - mid1
        l1,l2 = -1,-1
        r1,r2 = -1,-1
        if mid1  < n1:
            r1 = arr1[mid1]
        if mid2 < n2:
            r2 = arr2[mid2]
        if mid1-1 >=0:
            l1 = arr1[mid1-1]
        if mid2-1>=0:
            l2 = arr2[mid2-1]
        if l1<= r2 and l2 <= r1:
            if n%2 ==1:
                return max(l1,l2)
            return (max(l1,l2) + min(r1,r2)//2)
        elif l1 >r2:
            high = mid1-1
        else:
            low = mid1+1
def main():
    arr1 = [2,4,5,6]
    arr2 = [1,2,3,4]
    result = median_sorted_array(arr1,arr2)
    print(f"the median of two sorted array is : {result}")
if __name__=="__main__":
    main()



