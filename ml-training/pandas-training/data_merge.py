import pandas as pd

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 3, 5],
    "math": [85, 72, 95, 88]
})

print("----- Students -----")
print(students)

print("\n----- Scores -----")
print(scores)

print("")
print(pd.merge(students, scores))
print(pd.merge(students, scores, on="student_id"))
print(pd.merge(students, scores, on="student_id", how="left"))
print(pd.merge(students, scores, on="student_id", how="right"))
print(pd.merge(students, scores, on="student_id", how="inner"))
print(pd.merge(students, scores, on="student_id", how="outer"))
# left → 左邊全部留 right → 右邊全部留 inner → 兩邊都有才留 outer → 兩邊全部留
