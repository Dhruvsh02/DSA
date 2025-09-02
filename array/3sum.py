# 3 sum problem 
# brute force solution

def three_sum(arr):
    n = len(arr)
    ans = []
    set_map = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == 0:
                    temp= [arr[i], arr[j], arr[k]]
                    temp.sort()
                    set_map.add(tuple(temp))
    ans = [list(x) for x in set_map]
    return ans
def main():
    arr = [-1, 0, 1, 2, -1, -4]
    print(three_sum(arr))
if __name__ == "__main__":
    main()


# better solution using hashing

def three_sum(arr):
    n = len(arr)
    set_map = set()
    for i in range(n):
        count_map = {}
        for j in range(i+1,n):
            k = -(arr[i] + arr[j])
            if count_map.get(k, 0) > 0:
                temp = [arr[i], arr[j], k]
                temp.sort()
                set_map.add(tuple(temp))
            count_map[arr[j]] = count_map.get(arr[j], 0) + 1
    ans = [list(x) for x in set_map]
    return ans

def main():
    arr = [-1, 0, 1, 2, -1, -4]
    print(three_sum(arr))
if __name__ == "__main__":
    main()


# optimal solution using sorting and two pointers
def three_sum(arr):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                ans.append([arr[i],arr[j],arr[k]])
                j +=1
                k -=1 
                while j < k and arr[j] == arr[j-1]:
                    j += 1
                while j < k and arr[k] == arr[k+1]:
                    k -=1
    return ans

def main():
    arr = [-1, 0, 1, 2, -1, -4]
    print(three_sum(arr))
if __name__ == "__main__":  
    main()    
