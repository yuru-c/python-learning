import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score

# ROC Curve 是怎麼把不同 Threshold 的效果畫出來

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

model = LogisticRegression()
model.fit(x, y)
y_proba = model.predict_proba(x)[:, 1]
print("P(1):")
print(y_proba)

threshold = 0.5
y_pred = (y_proba >= threshold).astype(int)
print("Predicted:")
print(y_pred)

cm = confusion_matrix(y, y_pred)
print("Confusion Matrix:")
print(cm)

# Recall=TPR=TP/(TP+FN) 越高越好
# FPR=FP/(FP+TN) 越低越好 把實際的 0 錯判成 1 的比例
# ROC 不同Threshold下 Recall(TPR)和 False Positive Rate（FPR）之間的關係

fpr, tpr, thresholds = roc_curve(y, y_proba)
print("FPR:")
print(fpr)
print("TPR:")
print(tpr)
print("Thresholds:")
print(thresholds)

# ROC-AUC(Area Under the Curve) 這條曲線到底有多好？
# 1.0完美區分 0.5約等於隨機猜 < 0.5通常比隨機還差
auc = roc_auc_score(y, y_proba)
print("ROC-AUC:", auc)