import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# line plot

# subjects = ["Math", "English", "Science", "History", "Physics"]
# scores = [85, 78, 92, 70, 88]
# X 軸 → subjects Y 軸 → scores
# plt.plot(subjects, scores, marker=".", linestyle=":")
# o s ^
#"-" → 實線 "--" → 虛線 "-." → 點畫線 ":" → 點線
# plt.title("Student Scores")
# plt.xlabel("Subject")
# plt.ylabel("Score")


# subjects = ["Math", "English", "Science", "History", "Physics"]
# class_a = [85, 78, 92, 70, 88]
# class_b = [75, 85, 80, 90, 82]
# # help(plt.legend)
# plt.plot(subjects, class_a, label="Class_a")
# plt.plot(subjects, class_b, label="Class_b")
# plt.legend()
# plt.show()


# bar chart
# subjects = ["Math", "English", "Science", "History", "Physics"]
# scores = [85, 78, 92, 70, 88]
# plt.bar(subjects, scores)
# plt.title("Student Scores")
# plt.xlabel("Subject")
# plt.ylabel("Score")
# plt.show()


# scatter plot散佈圖
# hours = [1, 2, 3, 4, 5, 6, 7, 8]
# scores = [52, 58, 65, 67, 72, 78, 84, 91]
# plt.scatter(hours, scores)
# plt.show()


# Histogram 直方圖
# scores = [
#     52, 58, 61, 64, 65,
#     67, 68, 70, 72, 73,
#     74, 75, 76, 78, 80,
#     82, 84, 85, 87, 91
# ]
# plt.hist(scores, bins=10)
# # 把整個資料範圍切成 10 個區間
# bin_edges = [50, 60, 70, 80, 90, 100]
# plt.hist(scores, bins=bin_edges)
# # 每 10 分一組 從 50 到 100
# plt.show()


# subplots
# bar chart / line chart
# subjects = ["Math", "English", "Science", "History", "Physics"]
# scores = [85, 78, 92, 70, 88]
# fig, (ax1, ax2) = plt.subplots(1, 2)
# # nrows=1, ncols=2
# ax1.bar(subjects, scores)
# ax1.set_title("Student Scores - Bar")
# ax1.set_xlabel("Subject")
# ax1.set_ylabel("Score")
# ax2.plot(subjects, scores)
# ax2.set_title("Student Scores - Line")
# ax2.set_xlabel("Subject")
# ax2.set_ylabel("Score")
# # 標題字擠在一起用tight_layout()
# plt.tight_layout()
# plt.show()


# pandas numpy
# students = pd.DataFrame({
#     "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#     "math": [85, 72, 95, 68, 88],
#     "english": [90, 80, 88, 75, 92]
# })

# subjects = {
#     "math": (85, 72, 95, 68, 88),
#     "english": (90, 80, 88, 75, 92)
# }

# # res = ax.grouped_bar(subjects, tick_labels=students["name"])
# # for container in res.bar_containers:
# #     ax.bar_label(container)

# # plt.bar(students["name"], students["math"], label="Math")
# # plt.bar(students["name"], students["english"], label="English")
# names = ["Alice", "Bob", "Charlie", "David", "Eva"]
# x = np.arange(len(names))
# width = 0.4
# fig, ax = plt.subplots()
# ax.bar(x - width * 0.5,students["math"], width, label="Math")
# ax.bar(x + width * 0.5,students["english"], width, label="English")
# ax.set_xlabel("Names")
# ax.set_ylabel("Scores")
# ax.set_xticks(x)
# # 刻度要放在哪裡
# ax.set_xticklabels(names)
# # 刻度上要顯示什麼文字
# plt.legend()
# plt.show()


# students = pd.DataFrame({
#     "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#     "math": [85, 72, 95, 68, 88],
#     "english": [90, 80, 88, 75, 92],
#     "science": [78, 81, 94, 70, 86]
# })

# names = ["Alice", "Bob", "Charlie", "David", "Eva"]

# fig, (ax1, ax2) = plt.subplots(1, 2)
# x = np.arange(len(names))
# width = 0.2
# ax1.bar(x - width, students["math"], width, label="Math")
# ax1.bar(x, students["english"], width, label="English")
# ax1.bar(x + width, students["science"], width, label="Science")
# ax1.legend()
# ax1.set_xticks(x)
# ax1.set_xticklabels(names)

# students["average"] = students[["math", "english", "science"]].mean(axis=1)
# ax2.plot(students["name"], students["average"])

# ax2.set_title("Mean")
# plt.tight_layout()
# plt.show()



students = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "math": [85, 72, 95, 68, 88],
    "english": [90, 80, 88, 75, 92],
    "science": [78, 81, 94, 70, 86]
})

students["average"] = students[["math", "english", "science"]].mean(axis=1)
print(students.loc[students["average"].idxmax(), "name"])

fig, (ax1, ax2) = plt.subplots(1, 2)
x = np.arange(len(students["name"]))
width = 0.2
ax1.bar(x - width, students["math"], width, label="Math")
ax1.bar(x, students["english"], width, label="English")
ax1.bar(x + width, students["science"], width, label="Science")
ax1.set_xticks(x)
ax1.set_xticklabels(students["name"])
ax1.legend()
ax1.set_title("Student Scores")

ax2.plot(students["name"], students["average"], marker=".")
for _, row in students.iterrows():
    ax2.annotate(
        f"{row.average:.2f}",
        (row.name, row.average),
        xytext=(5, 3),
        textcoords="offset points"
    )
ax2.set_title("Average Score")
ax2.set_xlabel("Student")
ax2.set_ylabel("Average")

plt.tight_layout()
plt.show()