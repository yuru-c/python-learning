import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, classification_report
)
data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "sleep": [6, 7, 8, 7, 6, 8, 7, 8],
    "practice": [1, 1, 2, 2, 2, 3, 4, 5],
    "score": [52, 55, 65, 71, 74, 84, 90, 95]
}

df = pd.DataFrame(data)
df["passed"] = (df["score"] >= 70).astype(int)
# False = 0 / True = 1
print(df)

x = df[["hours", "sleep", "practice"]]
y = df["passed"]
print(x)
print(y)

# LogisticRegression -> Classification <Probability>

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)
# stratify=y 會盡量讓 Train / Test 都維持相似的類別比例

model_logistic = LogisticRegression()
model_logistic.fit(x_train, y_train)
y_pred = model_logistic.predict(x_test)
print("Actual:")
print(y_test)
print("Predicted:")
print(y_pred)

# Accuracy = 正確預測數/總預測數
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
# TP	實際 1，預測 1
# TN	實際 0，預測 0
# FP	實際 0，預測 1
# FN	實際 1，預測 0
# Precision = TP/(TP+FP) 模型說是 Pass 的人，有多少真的 Pass
precision = precision_score(y_test, y_pred)
print("Precision:", precision)
# Recall=TP/(TP+FN) 所有真正 Pass 的人裡面，模型成功找出了多少
recall = recall_score(y_test, y_pred)
print("Recall:", recall)
# Accuracy：全部猜對多少？
# Precision：我說「Pass」的，有多少真的 Pass？
# Recall：真的「Pass」裡，我抓到了多少？

# F1 Score F1=2*((Precision*Recall)/(Precision+Recall))
f1 = f1_score(y_test, y_pred)
print("F1 Score:", f1)

report = classification_report(y_test, y_pred)
print(report)
# support 測試資料中，實際屬於這個類別的樣本數

y_proba = model_logistic.predict_proba(x_test)
print("Probability:")
print(y_proba)
# [ P(0) -> 模型認為「屬於 0」的機率, P(1) -> 模型認為「屬於 1」的機率] 第 1 欄 → Fail 第 2 欄 → Pass
# Probability:
# [[0.00165566 -> fail 0.99834434 -> pass] -> pass機率超高
#  [0.42581471 -> fail 0.57418529 -> pass]]