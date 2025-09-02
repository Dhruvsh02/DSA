# longest palindrome substring 

def longest_palindrome(s):
    res= ''

    for i in range(len(s)):
        odd = expand(s,i,i)
        even = expand(s,i,i+1)
        res = max(res,odd,even,key=len)

    return res

def expand(s,left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -=1
        right +=1
    return s[left+1:right]

def main():
    s = 'babad'
    result = longest_palindrome(s)
    print(f"longest palindrome is : {result}")


if __name__=="__main__":
    main()