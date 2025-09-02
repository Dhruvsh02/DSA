# median in a row wise sorted matrix
# brute. approach 

def median(matrix):
    ls = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            ls.append(matrix[i][j])
    ls.sort()
    return ls[m*n//2]
def main():
    matrix = [[1,5,7,9,11],[2,3,4,5,10],[9,10,12,14,16]]
    result = median(matrix)
    print(f"median of row wise sorted matrix :{result}")
if __name__=="__main__":
    main() 


# optimal approach using binary search approach 

def upper_bound(mat,x):
    n = len(mat)
    low = 0 
    high = n-1
    ans = n
    while low <= high:
        mid = (low + high)//2
        if mat[mid] > x:
            ans = mid
            high = mid-1
        else:
            low = mid+1 
    return ans

def blackbox(mat,n,m,x):
    count = 0
    n = len(mat)
    for i in range(n):
        count += upper_bound(mat[i], x)
    return count 

def median(mat):
    n = len(mat)
    m = len(mat[0]) 
    req = (n*m)//2
    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)
    while low <= high:
        mid = (low+high)//2
        smaller_equals = blackbox(mat,n,m,mid)
        if smaller_equals <= req:
            low = mid+1
        else:
            high = mid-1
    return low 
def main():
    matrix = [[1,5,7,9,11],[2,3,4,5,10],[9,10,12,14,16]]
    result = median(matrix)
    print(f"median of row wise sorted matrix :{result}")
if __name__=="__main__":
    main() 