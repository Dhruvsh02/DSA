# ismorphic string 

def check(s,t):
    smap,tmap = [0] * 256 , [0] * 256
    n = len(s)
    for i in range(n):
        if smap[ord(s[i])] != tmap[ord(t[i])] :   # ord(c) is used to get ASCII value  converts char -> integers(ASCII code)
            return False 
        
        smap[ord(s[i])] = i+1
        tmap[ord(t[i])] = i+1
    return True 

def main():
    s = 'egg'
    t = 'add'
    result = check(s,t)
    print(f"ismorphic string true or false: {result}")
if __name__=="__main__":
    main()