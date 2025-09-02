# intersection of two sorted arrays ( brute force approach)

def intersection(a,b):
    vis= [0]*len(b)
    ans=[]
    for i in a:
        for j in range(len(b)):
            if i == b[j] and vis[j] == 0:
                ans.append(i)
                vis[j] = 1
                break
            if b[j] > a[i]:
                break
    return ans

def main():
    a = [1,2,3,3,3,4,5,6]
    b = [2,2,2,3,3,9,10]
    result = intersection(a, b)
    print("The intersection of the two arrays is: ", result)

if __name__ == "__main__":  
    main()

# 2 pointer approach(optimal)

def intersectionarr(a,b):
    i = 0
    j = 0
    ans = []
    while i <len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else: 
            ans.append(a[i])
            i += 1
            j += 1
    return ans

def main():
    a =[1,3,3,4,5,6,7,8,9]
    b =[3,4,5,6,7,8,9]
    result = intersectionarr(a, b)
    print("The intersection of the two arrays is: ", result)
if __name__ == "__main__":
    main()