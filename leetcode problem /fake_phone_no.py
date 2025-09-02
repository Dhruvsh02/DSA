# Fake Phone Number Validator 
# delta x question 
# This script validates phone numbers based on specific rules.
def is_valid(num):
     num = num.strip()
     if not num:
        return False
     digits_only = num.replace(" ", "")
     if len(num) < 10 or len(num) > 13:
         if " " in num and not (num[3] == " " and num[9] == " "):
                return False
         return False
     if num.startswith("+91"):
        if len(num) == 13 and num[3:].isdigit() and num[3:]:
             if " " in num and not (num[6] == " "):
                return False
             return True
     elif num.startswith("0"):
        if len(num) == 11 and num[1:].isdigit():
             if " " in num and not (num[5] == " "):
                return False
             return True
     elif num[0] in "789":
        if len(num) == 10 and num.isdigit():
             return True
     return False
def main():
    n = int(input("Enter number of phone numbers: ").strip())
    for _ in range(n):
        phone = input().strip()
        print("YES" if is_valid(phone) else "NO")


if __name__ == "__main__":
    main()



