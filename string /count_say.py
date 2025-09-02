# count and say 

def countandsay(n):
    if n == 1:
        return '1'
    prev = countandsay(n-1)
    count = 1 
    i = 1
    result = ''
    for i in range(1,len(prev)):
        if prev[i] == prev[i-1]:
            count+=1
        else:
            result += str(count)
            result += prev[i-1]
            count = 1
    
    result += str(count)
    result += prev[-1]
    return result

def main():
    n = 4
    result = countandsay(n)
    print(f"count and say of {n} is : {result}")
if __name__=="__main__":
    main()