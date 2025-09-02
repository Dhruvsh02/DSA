# check if the string is palindrome or not
'''
def palindrome(s,i,n):
    if i>=n/2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return palindrome(s,i+1,n)
def main():
    s=input("enter the string: ")
    i=0
    print(palindrome(s,i,len(s)))
if __name__ == "__main__":
    main()

'''
