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