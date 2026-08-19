import numpy as np

students = np.genfromtxt(
    "scores.csv", 
    delimiter=",", 
    skip_header=1,
    dtype=np.int32
)
# students= students.astype(np.int32)
print(students)

print("Shape:", students.shape)
print("Students:", students.shape[0])
print("Subjects:", students.shape[1])
print("第一個學生的成績:", students[0])
print("第一科所有學生的成績:", students[:,0])
print("所有學生的平均分:", students.mean())
print("每個學生的平均分:", students.mean(axis=1))
print("每個學生的最高分:", students.max(axis=1))
print("每個學生的最低分:", students.min(axis=1))
print("每科的平均分:", students.mean(axis=0))
print("平均分最高的學生是誰:", np.argmax(students.mean(axis=1))+1)