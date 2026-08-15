# def main():
#     X, Y = input("Fraction: ").strip().split("/")
#     fuel(X, Y)

# def fuel(x, y):
#     try:
#         X = int(x)
#         Y = int(y)
#         fraction = X / Y * 100
#         if 0 <= fraction <= 100:
#             if fraction == 100:
#                 print("F")
#             elif fraction == 0:
#                 print("E")
#             else:
#                 print(f"{fraction:.0f}%")
#         else:
#             main()
#     except (ValueError, ZeroDivisionError):
#         main()

# if __name__ == "__main__":
#     main()

# 原本程式
'''while True:
    try:
        X, Y = input("Fraction: ").strip().split("/")
        X = int(X)
        Y = int(Y)
        fraction = X / Y * 100
        if 0 <= fraction <= 100:
            if fraction == 100:
                print("F")
            elif fraction == 0:
                print("E")
            else:
                print(f"{fraction:.0f}%")
            break
    except (ValueError, ZeroDivisionError):
        pass'''


def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    X, Y = fraction.strip().split("/")
    X = int(X)
    Y = int(Y) 

    if Y == 0:
        raise ZeroDivisionError
    
    if X < 0 or X > Y:
        raise ValueError

    return X / Y * 100

def gauge(percentage):
    if percentage <= 1:
        return "E"  
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()