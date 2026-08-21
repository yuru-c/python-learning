import pandas as pd

# merge()
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
# left → 左邊全部留 right → 右邊全部留 
# inner（交集） → 兩邊都有才留 outer（聯集） → 兩邊全部留

# concat()
print("")
students_1 = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "math": [85, 72]
})

students_2 = pd.DataFrame({
    "name": ["Charlie", "David"],
    "math": [95, 68]
})

print(pd.concat([students_1, students_2], axis=0))
print(pd.concat([students_1, students_2], axis=0, ignore_index=True))

print("")
names = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"]
})

scores = pd.DataFrame({
    "math": [85, 72, 95],
    "english": [90, 80, 88]
})

print(pd.concat([names, scores], axis=1))

print("")
students_1 = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "math": [85, 72]
})

students_2 = pd.DataFrame({
    "name": ["Charlie", "David"],
    "english": [95, 68]
})

print(pd.concat([students_1, students_2], ignore_index=True).fillna(0))



students = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 3],
    "math": [85, 72, 95],
    "english": [90, 80, 88]
})

result = pd.merge(students, scores)
print(result)
result["average"] = result[["math", "english"]].mean(axis=1)
print(result)
print(result.loc[result["average"].idxmax(), "name"])