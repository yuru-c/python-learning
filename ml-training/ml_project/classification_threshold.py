import numpy as np

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score
)

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
thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
for threshold in thresholds:
    y_pred = (y_proba >= threshold).astype(int)
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)
    f1 = f1_score(y, y_pred)
    print(f"\nThreshold: {threshold}")
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1:", f1)