# 從CSV(Comma-Separated Values)以逗號分割
"""with open("students.csv") as file:
    for line in file:
        # row = line.rstrip().split(",")        
        # print(f"{row[0]} is in {row[1]}")
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")"""

# 排序 不好
"""students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)"""



# 排序
"""students = []
with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {}
        # student["name"] = name
        # student["house"] = house
        student = {"name":name, "home":home}
        students.append(student)

# def get_name(student):
#     return student["name"]

# def get_student(student):
#     return student["house"]

# for student in sorted(students, key=get_name):
# 匿名建立 lambda
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")"""

# CSV遇到value本身有,時
'''import csv
students = []
with open("students.csv") as file:
    # CSV前面沒有name,home
    """reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})"""
    # CSV前面有name,home CSV有很多values也可執行
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")'''

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a", newline="") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, home])
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
