# using 2 pointer 
'''
def reverse(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    reverse(arr,l+1,r-1)
def main():
    arr=[1,2,3,4,5,6,7]
    reverse(arr,0,len(arr)-1)
    print(arr)
if __name__ == "__main__": 
    main()
'''

# using 1 pointer 
'''
def reverse(arr,i):
    n=len(arr)
    if i>=n/2:
        return
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    reverse(arr,i+1)
def main():
    arr=[2,4,5,6,7,8]
    reverse(arr,0)
    print(arr)
if __name__ == "__main__":  
    main()

''' 