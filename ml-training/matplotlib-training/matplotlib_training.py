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
hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [52, 58, 65, 67, 72, 78, 84, 91]
plt.scatter(hours, scores)
plt.show()