import pandas as pd

students = pd.read_csv("scores.csv")

# print(students)
# print("Shape: ", students.shape)
# print("Columns: ", students.columns)
# print("Index: ", students.index)
# print(students.head())
# print(students.tail())
# print(students.describe())

# print("印出學生人數: ", students.shape[0])
# print("印出科目數: ", students.shape[1])
# print("印出所有科目名稱: ")
# for s in range(students.shape[1]):
#     print(students.columns[s], end=" ")
# print("")
# print("印出前 3 個學生: \n", students.head(3))
# print("印出最後 2 個學生: \n", students.tail(2))
# print("印出所有科目的平均分: \n", students.mean())

'''print("印出所有 Math 成績: \n", students["math"])
# [] series 一欄
print("印出 Math + English: \n", students[["math", "english"]])
# [[]] dataframe 多欄
print("Math 平均: ", students["math"].mean())
print("English 平均: ", students["english"].mean())
print("Science 平均: ", students["science"].mean())'''

# print("----- Subject Selection -----\n")
# print("Math: \n", students["math"])
# print("English: \n", students["english"])
# print("Science: \n", students["science"])
# print("\n----- Subject Statistics -----\n")
# print("Math Average: ", students["math"].mean())
# print("Math Maximum: ", students["math"].max())
# print("Math Minimum: ", students["math"].min())
# print("English Average: ", students["english"].mean())
# print("English Maximum: ", students["english"].max())
# print("English Minimum: ", students["english"].min())

'''# iloc位置
print("----- iloc -----\n")
print("第 1 個學生: \n", students.iloc[0])
print("前 3 個學生: \n", students.iloc[0:3])
print("第 1 科: \n", students.iloc[:, 0])
print("前 3 個學生的前 2 科: \n", students.iloc[0:3, 0:2])

# loc標籤
print("----- loc -----\n")
print("第 1 個學生: \n", students.loc[0])
print("所有學生的 Math: \n", students.loc[:, "math"])
print("前 3 個學生的 Math + English: \n", students.loc[0:2, ["math","english"]])'''

'''print("----- Filtering -----\n")
print("Math >= 80:")
print(students[students["math"] >= 80])
print("\nMath < 60:")
print(students[students["math"] < 60])
print("\nEnglish >= 90:")
print(students[students["english"] >= 90])
print("\nMath >= 80 AND English >= 80:")
print(students[
    (students["math"] >= 80) &
    (students["english"] >= 80)
])
print("\nMath >= 90 OR English >= 90:")
print(students[
    (students["math"] >= 90) |
    (students["english"] >= 90)
])'''

'''print("----- Sorting -----\n")
# print("Math 由低到高:")
# print(students.sort_values("math", ascending=True))
# print("Math 由高到低:")
# print(students.sort_values("math", ascending=False))
# print("\nMath 前 3 名:")
# print(students.sort_values("math", ascending=False).head(3))
# # 如果 Math 一樣 → English 高 → 低
# print("\nMath → English 排序:")
# print(
#     students.sort_values(
#         ["math", "english"],
#         ascending=[False, False]
#     )
# )
print("Math 最高的學生:\n", students.sort_values("math", ascending=False).head(1))
print("\nEnglish 最低的 3 個學生:")
print(students.sort_values("english", ascending=True).head(3))
print("\nMath 和 English 都 ≥ 80 的學生，並按照 Math 由高到低排序:")
print(students[
    (students["math"] >= 80) & 
    (students["english"] >= 80)].sort_values("math", ascending=False))'''

'''print("----- Value Counts -----\n")
print("Computer 成績出現次數:")
print(students["computer"].value_counts())
print("\nComputer 前 5 個最常出現的成績:")
print(students["computer"].value_counts().head(5))
print(students["computer"].value_counts().head(1))
# 最高頻率的分數本身
print(students["computer"].value_counts().index[0])
# 最高頻率是多少次
print(students["computer"].value_counts().iloc[0])'''

# 新增一個欄位
students["grade"] = pd.cut(
    students["math"],
    bins=[0, 59, 69, 79, 89, 100],
    labels=["F", "D", "C", "B", "A"]
)

print(students[["math", "grade"]])
print(students.groupby("grade").size())
print(students.groupby("grade")["math"].mean())
print(
    students.groupby("grade")["math"].agg(
        ["mean", "max", "min"]
    )
)
print(students.groupby("grade")["math"].mean().idxmax())
print(students.groupby("grade")[["math", "english", "science"]].mean())

students["average"] = students[["math", "english", "science"]].mean(axis=1)
print(students)
print(students.sort_values("average", ascending=False).head(1))
print(students.sort_values("average").head(1))
print(students[students["average"] >= 80])
print(students.sort_values("average", ascending=False).head(3)[["math", "english", "science", "average"]]
)