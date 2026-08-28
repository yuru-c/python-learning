import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

x = np.array([
    [1, 7],
    [2, 6],
    [3, 8],
    [4, 7],
    [5, 6],
    [6, 8],
    [7, 7],
    [8, 8]
])

y = np.array([
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1
])

# Accuracy=(TP+TN)/(TP+TN+FP+FN) 總共有多少比例預測正確？
model = LogisticRegression()
scores = cross_val_score(
    model, x, y, cv=4, scoring="accuracy"
)
print("Scores:", scores)
print("Mean Accuracy:", scores.mean())

# F1=2(Precision*Recall)/(Precision+Recall)
model = LogisticRegression()
scores_f1 = cross_val_score(
    model, x, y, cv=4, scoring="f1"
)
print("F1 Scores:", scores_f1)
print("Mean F1:", scores_f1.mean())