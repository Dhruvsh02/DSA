# Union of two sorted arrays(brute force approach)
def union(n,m):
    s = set()
    for i in n:
        s.add(i)
    for i in m:
        s.add(i)
    temp = []
    for i in sorted(s):
        temp.append(i)
    
    return temp

def main():
    n=[1,2,3,4,5,6,7,7,7,7]
    m=[2,3,4,5,6,7,8,9]
    result = union(n,m)
    print("The union of the two arrays is: ", result)
if __name__ == "__main__":
    main() 

# optimal approach 

def union_array(a,b,union_arr):
    n1 = len(a)
    n2 = len(b)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if a[i] <= b[j]:
            if not union_arr or a[i] != union_arr[-1]:
                union_arr.append(a[i])
            i += 1
        elif b[j] < a[i]:
            if not union_arr or b[j] != union_arr[-1]:
                union_arr.append(b[j])
            j += 1
        else:
            if not union_arr or a[i] != union_arr[-1]:
                union_arr.append(a[i])
            i += 1
            j += 1
    
    while j < n2:
        if not union_arr or b[j] != union_arr[-1]:
            union_arr.append(b[j])
        j += 1
    while i < n1:
        if not union_arr or a[i] != union_arr[-1]:
            union_arr.append(a[i])
        i += 1
    return union_arr
def main():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    union_arr = []
    result = union_array(a,b,union_arr)
    print("The union of the two arrays is: ", result)
if __name__ == "__main__":
    main()


