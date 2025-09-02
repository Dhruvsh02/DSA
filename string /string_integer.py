# string to integer (atoi)

def string_to_integer(s):
    i = 0
    n = len(s)
    # step 1 is to remove leading spaces
    while i < n and s[i] == ' ':
        i+=1
    # step 2 is to check for sign
    sign = 1
    if i < n and s[i] == '-':
        sign = -1
        i+=1
    elif i < n and s[i] == '+':
        i+=1
    
    # step 3 is to convert number and avoid overflow
    result = 0
    while i < n and s[i].isdigit():
        result = result * 10 + (ord(s[i]) - ord('0'))
        i+=1 

        if result * sign >= s**31-1:
            return 2**31-1
        if result*sign <= -2**31:
            return -2**31
        
    return result * sign

def main():
    s = "   -42"
    result = string_to_integer(s)
    print(f"string to integer is : {result}")
if __name__ == "__main__":
    main()
