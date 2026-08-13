months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

# def main():
#     while True:    
#         try:
#             date = input("Date: ").strip()
#             if "/" in date:
#                 M, D, Y = date.split("/")            
#                 M = int(M)
#                 D = int(D)
#                 Y = int(Y)
#                 if mdy(M, D, Y):
#                     print(f"{Y:04}-{M:02}-{D:02}")
#                     break
#             else:
#                 M, D, Y = date.split()
#                 D = D.removesuffix(",")
#                 M = months.index(M) + 1
#                 D = int(D)
#                 Y = int(Y)
#                 if mdy(M, D, Y):
#                     print(f"{Y:04}-{M:02}-{D:02}")
#                     break
#         except (ValueError, EOFError):
#             pass

# def mdy(m, d, y):
#     if not 1 <= m <= 12:
#         return False
#     if m == 2:
#         if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#             if not 1 <= d <= 29:
#                 return False
#         else:
#             if not 1 <= d <= 28:
#                 return False
#     elif m in (1, 3, 5, 7, 8, 10, 12):
#         if not 1 <= d <= 31:
#             return False
#     elif m in (4, 6, 9, 11):
#         if not 1 <= d <= 30:
#             return False
#     return True

# if __name__ == "__main__":
#     main()

def main():
    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            else:
                month, day, year = date.split()
                day = int(day.removesuffix(","))
                month = months.index(month) + 1
                year = int(year)

            if valid_date(month, day, year):
                print(f"{year:04}-{month:02}-{day:02}")
                break

        except (ValueError, EOFError):
            pass


def valid_date(month, day, year):
    if not 1 <= month <= 12:
        return False

    days = [
        31,
        29 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    ]

    return 1 <= day <= days[month - 1]


if __name__ == "__main__":
    main()