# 4 sum problem 
# brute force solution

def four_sum(arr, target):
    n = len(arr)
    ans =[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        temp.sort()
                        if temp not in ans:
                            ans.append(temp)
    return ans
def main():
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    print(four_sum(arr, target))
if __name__ == "__main__":
    main()

# better solution using hashing

def four_sum(arr, target):
    n = len(arr)
    ans = []
    set_map = set()
    for i in range(n):
        count_map = {}
        for j in range(i+1,n):
            for k in range(j+1,n):
                l = target - (arr[i]+arr[j]+arr[k])
                if count_map.get(l, 0) > 0:
                    temp = [arr[i],arr[j],arr[k],l]
                    temp.sort()
                    set_map.add(tuple(temp))
                count_map[arr[k]] = count_map.get(arr[k], 0) + 1
    ans = [list(x) for x in set_map]
    return ans
def main(): 
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    print(four_sum(arr, target))
if __name__ == "__main__":
    main()

# optimal solution using sorting and two pointers

def four_sum(arr, target):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            k = j+1
            l = n-1
            while k < l:
                sum = arr[i] + arr[j] + arr[k] + arr[l]
                if sum == target:
                    ans.append([arr[i], arr[j], arr[k], arr[l]])
                    k += 1
                    l -= 1
                    while k < l and arr[k] == arr[k-1]:
                        k +=1
                    while k < l and arr[l] == arr[l+1]:
                        l -=1
                elif sum < target:
                    k += 1
                else:
                    l -= 1
    return ans
def main():
    arr = [1,1,1,2,2,2,3,3,3,4,4,4,5,5]
    target = 8
    print(four_sum(arr, target))
if __name__ == "__main__":
    main()