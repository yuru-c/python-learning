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


while True:
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
        pass