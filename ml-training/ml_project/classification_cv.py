import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier

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

# F1=2(Precision*Recall)/(Precision+Recall) Precision 和 Recall 的平衡如何？
model = LogisticRegression()
scores_f1 = cross_val_score(
    model, x, y, cv=4, scoring="f1"
)
print("F1 Scores:", scores_f1)
print("Mean F1:", scores_f1.mean())


# ROC-AUC 模型區分 Class 0 / Class 1 的能力如何？
cv = StratifiedKFold(
    n_splits=3, shuffle=True, random_state=42
)
# 會盡量維持每個 Fold 都有 0 和 1
scores_auc = cross_val_score(
    model, x, y, cv=cv, scoring="roc_auc"
)
print("ROC-AUC Scores:", scores_auc)
print("Mean ROC-AUC:", scores_auc.mean())

# accuracy
logistic = LogisticRegression()
knn = KNeighborsClassifier(n_neighbors=3)

logistic_scores = cross_val_score(
    logistic, x, y, cv=cv, scoring="accuracy"
)
print("Logistic Regression:")
print("Scores:", logistic_scores)
print("Mean Accuracy:", logistic_scores.mean())

knn_scores = cross_val_score(
    knn, x, y, cv=cv, scoring="accuracy"
)
print("KNN:")
print("Scores:", knn_scores)
print("Mean Accuracy:", knn_scores.mean())

# f1
logistic_scores_f1 = cross_val_score(
    logistic, x, y, cv=cv, scoring="f1"
)
print("Logistic Regression:")
print("F1 Scores:", logistic_scores_f1)
print("Mean F1:", logistic_scores_f1.mean())

knn_scores_f1 = cross_val_score(
    knn, x, y, cv=cv, scoring="f1"
)
print("KNN:")
print("F1 Scores:", knn_scores_f1)
print("Mean F1:", knn_scores_f1.mean())

# roc-auc
logistic_scores_auc = cross_val_score(
    logistic, x, y, cv=cv, scoring="roc_auc"
)
print("Logistic Regression:")
print("ROC-AUC Scores:", logistic_scores_auc)
print("Mean ROC-AUC:", logistic_scores_auc.mean())

knn_scores_auc = cross_val_score(
    knn, x, y, cv=cv, scoring="roc_auc"
)
print("KNN:")
print("ROC-AUC Scores:", knn_scores_auc)
print("Mean ROC-AUC:", knn_scores_auc.mean())