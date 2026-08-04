"""while True:    
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")"""



def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

"""def get_int():
    while True:    
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        # 沒有else 會 NameError: name 'x' is not defined
        else:
            # break
            return x
    # return x"""


def get_int(prompt):
    while True:    
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()