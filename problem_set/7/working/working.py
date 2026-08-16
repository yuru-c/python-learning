import re

def main():
    print(convert(input("Hours: ")))

# def convert(s):
#     if matches := re.search(r"(0?[1-9]|1[0-2])(:[0-5][0-9])? (A|P)M to (0?[1-9]|1[0-2])(:[0-5][0-9])? (A|P)M", s):
#         hour1 = matches.group(1)
#         if matches.group(2):
#             minute1 = matches.group(2).removeprefix(":")
#         period1 = matches.group(3)
#         hour2 = matches.group(4)
#         if matches.group(5):
#             minute2 = matches.group(5).removeprefix(":")
#         period2 = matches.group(6)
#         if period1 == "A" and int(hour1) == 12:
#             hour1 = "00"
#         if period1 == "P" and int(hour1) != 12:
#             hour1 = str(int(hour1) + 12)
#         if len(hour1) < 2:
#             hour1 = "0" + hour1
#         if not matches.group(2):
#             minute1 = "00"

#         if period2 == "A" and int(hour2) == 12:
#             hour2 = "00"
#         if period2 == "P" and int(hour2) != 12:
#             hour2 = str(int(hour2) + 12)
#         if len(hour2) < 2:
#             hour2 = "0" + hour2
#         if not matches.group(5):
#             minute2 = "00"

#         return f"{hour1}:{minute1} to {hour2}:{minute2}"
#     else:
#         raise ValueError

'''re.search(r"^...$", s) = re.fullmatch(...)'''

def convert(s):
    matches = re.fullmatch(
        r"(0?[1-9]|1[0-2])(?::([0-5][0-9]))? ([AP]M) "
        r"to "
        r"(0?[1-9]|1[0-2])(?::([0-5][0-9]))? ([AP]M)",
        s
    )
    # 冒號要匹配，但不要捕獲；分鐘要匹配，而且要捕獲

    if not matches:
        raise ValueError

    hour1, minute1, period1, hour2, minute2, period2 = matches.groups()

    hour1 = convert_hour(hour1, period1)
    hour2 = convert_hour(hour2, period2)

    minute1 = minute1 or "00"
    minute2 = minute2 or "00"
    # minute1 = None → "00"

    return f"{hour1:02}:{minute1} to {hour2:02}:{minute2}"


def convert_hour(hour, period):
    hour = int(hour)

    if period == "AM" and hour == 12:
        hour = 0
    elif period == "PM" and hour != 12:
        hour += 12

    return hour


if __name__ == "__main__":
    main()