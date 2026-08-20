import pandas as pd

students = pd.DataFrame({
    "name" : ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "grade" : ["A", "B", "A", "C", "B", "C"],
    "math" : [95, 82, 88, 70, 76, 65],
    "english": [90, 85, 92, 68, 80, 72],
    "science": [93, 78, 90, 75, 82, 70]
})

print(students)
print(students.groupby("grade").size())
print(students.groupby("grade")["math"].mean())
print(students.groupby("grade")["math"].agg(
    ["mean", "max", "min"]
))
print(students.groupby("grade")[["math", "english", "science"]].mean())
print(students.groupby("grade")[["math", "english", "science"]].agg(
    ["mean", "max", "min"]
))
print(students.groupby("grade")["math"].mean().idxmax())
students["average"] = students[["math", "english", "science"]].mean(axis=1)
print(students)
print(students.loc[students.groupby("grade")["average"].idxmax(), "name"])