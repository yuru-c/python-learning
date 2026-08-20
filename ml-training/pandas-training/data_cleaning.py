import numpy as np
import pandas as pd


data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "math": [85, 72, 95, np.nan],
    "english": [90, np.nan, 88, 75],
    "science": [78, 81, np.nan, 92]
}

students = pd.DataFrame(data)

print(students)

print("\n----- Missing Count -----")
print(students.isna().sum())
# isna() 找出缺失值

print("\n----- Drop Missing -----")
print(students.dropna())
# dropna() 只要一列裡面有 NaN，就把整列刪掉。
print(students.dropna(axis=1))
# dropna(axis=1) 只要某一欄有 NaN，就把整個欄位刪掉。

print("\n----- Fill Missing -----")
print(students.fillna(0))
# fillna() 填補缺失值
for column in ["math", "english", "science"]:
    students[column] = students[column].fillna(
    students[column].mean()
)
print(students.round(2))

print("\n----- Duplicate Data -----")
duplicate_data = {
    "name" : ["Alice", "Bob", "Charlie", "Alice", "Bob"],
    "math" : [85, 72, 95, 85, 72],
    "english" : [90, 75, 88, 95, 75]
}

scores = pd.DataFrame(duplicate_data)

print(scores)

print("\n----- Duplicates -----")
print(scores.duplicated())

print("\n----- Remove Duplicates -----")
clean_scores = scores.drop_duplicates()
print(clean_scores)
print("original:", len(scores))
print("Clean:", len(clean_scores))
print(scores.drop_duplicates(subset=["name"]))
print(scores.drop_duplicates(keep="first"))
# 保留第一次出現的 Alice 刪掉後面的 Alice
print(scores.drop_duplicates(subset=["name"], keep="last"))
# 保留最後一次
print(scores.drop_duplicates(subset=["name"], keep=False))
# 只要某個 name 出現超過一次 全部刪掉
print(students.dtypes)
print(students)
students["math"] = students["math"].astype(int)
students["english"] = students["english"].astype(int)
students["science"] = students["science"].astype(int)
print(students.dtypes)

dirty_data = {
    "name" : ["Alice", "Bob", "Charlie", "Alice", "David", "Eve"],
    "math" : [85, 72, np.nan, 85, 91, 68],
    "english" : [90, np.nan, 88, 90, 95, 70],
    "science" : [78, 81, 92, 78, np.nan, 65]
}

dirty_students = pd.DataFrame(dirty_data)

print("\n----- Dirty Data -----")
print(dirty_students)
print(dirty_students.isna().sum())
print(dirty_students.duplicated())
for column in ["math", "english", "science"]:
    dirty_students[column] = dirty_students[column].fillna(
        dirty_students[column].mean()
    )
print(dirty_students.drop_duplicates(subset=["name"]))
for column in ["math", "english", "science"]:
    dirty_students[column] = dirty_students[column].round().astype(int)

dirty_students["average"] = dirty_students[
    ["math", "english", "science"]
].mean(axis=1)

dirty_students = dirty_students.sort_values(
    "average", ascending=False
)
print("\n----- Clean Data -----")
print(dirty_students)