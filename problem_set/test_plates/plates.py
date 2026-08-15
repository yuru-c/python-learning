# 原本程式
'''def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
    #     for i in range(len(s) - 1):
    #         if s[i].isnumeric() and s[i+1].isalpha():
    #             return False
    #     for p in s:
    #         if p.isdigit():
    #             if p == "0":
    #                 return False 
    #             break
    #     return True        
    # else:
    #     return False


    if not 2 <= len(s) <=6:
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            break

    return True'''

# 為test_plates修改
def main():
    plate = input("Plate: ")
    print(is_valid(plate))

def is_valid(s):
    if not 2 <= len(s) <=6:
        return "Invalid"

    if not s[:2].isalpha():
        return "Invalid"

    if not s.isalnum():
        return "Invalid"

    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return "Invalid"

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return "Invalid"
            break

    return "Valid"

if __name__ == "__main__":
    main()