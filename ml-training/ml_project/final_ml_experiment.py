import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("student_data.csv")

x = df[["hours", "attendance", "assignments"]].values
y = df["passed"].values

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42, stratify=y
)

# print("X Train:")
# print(x_train)
# print("X Test:")
# print(x_test)
# print("Y Train:")
# print(y_train)
# print("Y Test:")
# print(y_test)

logistic = Pipeline([
    ("scaler", StandardScaler()),
    ("logistic", LogisticRegression())
])

knn = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=3))
])

logistic_scores = cross_val_score(
    logistic, x_train, y_train, cv=3, scoring="accuracy"
)

knn_scores = cross_val_score(
    knn, x_train, y_train, cv=3, scoring="accuracy"
)

logistic_f1 = cross_val_score(
    logistic, x_train, y_train, cv=3, scoring="f1"
)

knn_f1 = cross_val_score(
    knn, x_train, y_train, cv=3, scoring="f1"
)

logistic_auc = cross_val_score(
    logistic, x_train, y_train, cv=3, scoring="roc_auc"
)

knn_auc = cross_val_score(
    knn, x_train, y_train, cv=3, scoring="roc_auc"
)

print("Logistic Regression:")
print("Accuracy:", logistic_scores.mean())
print("F1:", logistic_f1.mean())
print("ROC-AUC:", logistic_auc.mean())

print()

print("KNN:")
print("Accuracy:", knn_scores.mean())
print("F1:", knn_f1.mean())
print("ROC-AUC:", knn_auc.mean())