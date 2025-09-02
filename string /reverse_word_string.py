# reverse every word in a string / palindrome check 
# brute force approach 

def reverse(s):
    ans = []
    i = 0
    n = len(s)
    while i<n:
        while i < n and s[i] == ' ' :
            i+=1
        if i >= n:
            break 
        j = i
        while j < n and s[j]!= ' ':
            j+=1
        ans.append(s[i:j])
        i = j
        result =""
        for k in range(len(ans) -1,-1,-1):
            result += ans[k]
            if k > 0:
                result += " "

    return result 
def main():
    s = " the sky is red "
    result = reverse(s)
    print(result)
if __name__=="__main__":
    main()

# optimal approach 

def reverse_string(s,start,end):
    while start < end:
        s[start],s[end] = s[end],s[start]
        start+=1
        end-=1
def reverse_word(s):
    n = len(s)
    s = list(s)
    reverse_string(s,0,n-1)
    i,j = 0,0
    while j < n:
        while j < n and s[j] == ' ':
            j+=1
        if j == n:
            break
        start = i
        while j < n and s[j] != ' ':
            s[i] = s[j]
            i+=1
            j+=1
        end = i-1
        reverse_string(s,start,end)
        if j < n:
            s[i] = ' '
            i+=1
    if i > 0 and s[i-1] == ' ':
        i-=1
    return "".join(s[:i])
def main():
    s = " the sky is red "
    result = reverse_word(s)
    print(result)
if __name__=="__main__":
    main()

# optimalized with best complexity
def reverse(s):
    return " ".join(s.split()[::-1])
