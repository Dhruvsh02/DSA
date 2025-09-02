# roman number to integer

def romanToInt(s: str) -> int:
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)
    for i in range(n):
        if i+1 < n and roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total

def main():
    s = "MCMXCIV"
    result = romanToInt(s)
    print(f"roman to integer is : {result}")
if __name__ == "__main__":
    main()


# integer to roman number

def intToRoman(num: int) -> str:
    values = [(1000,"M"), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40,"XL"), (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")]

    res = []

    for val,sym in values:
        while num >= val:
            res.append(sym)
            num -= val 
    return "".join(res)
def main():
    num = 1994
    result = intToRoman(num)
    print(f"integer to roman is : {result}")
if __name__ == "__main__":
    main()