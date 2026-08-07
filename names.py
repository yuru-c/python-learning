# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What's your name? ")

# "w" is write , "a" is append
"""file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()"""

# "with" call funtction 自動關閉檔案, "as" 指定var 賦予open的返回值
"""with open("names.txt", "a") as file:
    file.write(f"{name}\n")"""

# "r" 讀取 載入 非儲存
"""with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    # print("hello,", line, end="")
    print("hello,", line.rstrip())
    # rstrip 剝掉\n設定"""

# 簡化讀取
"""with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())"""

# 排序資料 可以先存到list 排序在列印
names = []

with open("names.txt") as file:
    for line in file:
        # 加到list 不是檔案
        names.append(line.rstrip())

    # for name in sorted(names):
    for name in sorted(names, reverse=True):
        print(f"hello, {name}")


# 排序簡化
"""with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())"""

