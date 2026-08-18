import numpy as np

'''scores = np.array([67, 45, 91, 82, 56, 73, 100, 38])

sorted_scores = np.sort(scores)

print(sorted_scores)
print("前三名", sorted_scores[-3:][::-1])
# [開始 : 結束 : 步長]
print("最後三名",sorted_scores[:3])
# print("中位數", np.median(sort))
print("中位數", np.median(scores))
# 不重複值
# values, counts = np.unique(sort, return_counts=True)
values, counts = np.unique(scores, return_counts=True)
print("眾數", values[np.argmax(counts)])'''


'''scores = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [90, 95, 88],
    [70, 65, 72]
])

print("每個學生的成績由低到高排序", np.sort(scores, axis=1))
print("每個學生的最高分", np.sort(scores, axis=1)[:,-1])
print("每科由低到高排序", np.sort(scores, axis=0))
# print("每科最高分", np.sort(scores, axis=0)[-1,:])
print("每科最高分", scores.max(axis=0))'''


scores = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [90, 95, 88],
    [70, 65, 72]
])

# student_avg = scores.mean(axis=1)
# subject_avg = scores.mean(axis=0)

# best_student = np.argmax(student_avg) + 1
# best_subject = np.argmax(subject_avg) + 1

print("每個學生的平均分", np.mean(scores, axis=1))
print("每科的平均分", np.mean(scores, axis=0))
print("平均分最高的學生", np.argmax(np.mean(scores, axis=1))+1)
print("平均分最高的是哪一科", np.argmax(np.mean(scores, axis=0))+1)