import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import (
    train_test_split, StratifiedKFold, cross_val_score, GridSearchCV
)
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score
)

df = pd.read_csv("data/student-mat.csv", sep=";")

# print("Shape:")
# print(df.shape)
# print("\nFirst 5 rows:")
# print(df.head())
# print("\nColumns:")
# print(df.columns.tolist())
# print("\nInfo:")
# print(df.info())
# print("\nDescribe:")
# print(df.describe())

df["passed"] = (df["G3"] >= 10).astype(int)
print("Passed distribution:")
print(df["passed"].value_counts())
print("\nG3 vs Passed:")
print(df[["G3", "passed"]].head(20))
print(df.groupby("passed")["G3"].agg(["count", "min", "mean"]))

# Model A G1 + G2
X_with_grades = df.drop(columns=["G3", "passed"])
y = df["passed"]

# Model B No G1/G2
X_without_grades = df.drop(columns=["G1", "G2", "G3", "passed"])

# print("Categorical columns:")
# print(X_with_grades.select_dtypes(include="object").columns.tolist())

# print("\nNumeric columns:")
# print(X_with_grades.select_dtypes(exclude="object").columns.tolist())

categorical_features = X_with_grades.select_dtypes(
    include="object"
).columns

numeric_features = X_with_grades.select_dtypes(
    exclude="object"
).columns

preprocessor = ColumnTransformer(
    # 指定「哪些欄位要做什麼處理」
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            # 把「類別型文字」轉成 0/1 的欄位
            # 遇到新的類別直接忽略
            categorical_features,
        ),
        (
            "num",
            "passthrough",
            numeric_features,
        )
    ]
)

# Logistic Regression pipeline
logistic_model = Pipeline([
    ("preprocessor", preprocessor),
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

# KNN pipeline
knn_model = Pipeline([
    ("preprocessor", preprocessor),
    ("scaler", StandardScaler()),
    ("model", KNeighborsClassifier(n_neighbors=5))
])

print("Pipelines created successfully.")

X_train, X_test, y_train, y_test = train_test_split(
    X_with_grades, y, test_size=0.2, random_state=42, stratify=y
)

print("Training set:", X_train.shape)
print("Test set:", X_test.shape)

print("\nTraining target distribution:")
print(y_train.value_counts())

print("\nTest target distribution:")
print(y_test.value_counts())

baseline = DummyClassifier( 
    strategy="most_frequent"
    # 永遠猜訓練資料中出現最多的類別
)

baseline.fit(X_train, y_train)
baseline_pred = baseline.predict(X_test)


# Train Logistic Regression
logistic_model.fit(X_train, y_train)
# Predict
logistic_pred = logistic_model.predict(X_test)
# Accuracy
logistic_accuracy = accuracy_score(
    y_test, logistic_pred
)
print("\nLogistic Regression Accuracy:")
print(logistic_accuracy)

# Train KNN
knn_model.fit(X_train, y_train)
# Predict
knn_pred = knn_model.predict(X_test)
# Accuracy
knn_accuracy = accuracy_score(
    y_test, knn_pred
)
print("\nKNN Accuracy:")
print(knn_accuracy)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

logistic_cv_scores = cross_val_score(
    logistic_model, X_train, y_train, cv=cv, scoring="accuracy"
)
print("\nLogistic Regression CV Accuracy:")
print(logistic_cv_scores)
print("Mean:", logistic_cv_scores.mean())

knn_cv_scores = cross_val_score(
    knn_model, X_train, y_train, cv=cv, scoring="accuracy"
)
print("\nKNN CV Accuracy:")
print(knn_cv_scores)
print("Mean:", knn_cv_scores.mean())

param_grid = {
    "model__n_neighbors": [3, 5, 7, 9]
}

grid_search = GridSearchCV(
    knn_model, param_grid, cv=cv, scoring="accuracy"
)

grid_search.fit(X_train, y_train)
print("\nBest K:")
print(grid_search.best_params_)
print("\nBest CV Accuracy:")
print(grid_search.best_score_)
best_knn = grid_search.best_estimator_

baseline_accuracy = accuracy_score(
    y_test, baseline_pred
)
logistic_accuracy = accuracy_score(
    y_test, logistic_pred
)
best_knn_pred = best_knn.predict(X_test)
best_knn_accuracy = accuracy_score(
    y_test, best_knn_pred
)
print("\n===== Model Comparison =====")
print("Baseline:", baseline_accuracy)
print("Logistic Regression:", logistic_accuracy)
print("Best KNN:", best_knn_accuracy)
print("\n===== CV Comparison =====")
print(
    "Logistic Regression CV Mean:",
    logistic_cv_scores.mean()
)
print(
    "Best KNN CV Mean:",
    grid_search.best_score_
)

final_model = logistic_model
final_model.fit(X_train, y_train)
final_pred = final_model.predict(X_test)
print("\nFinal Model:")
print("Logistic Regression")
print("\nFinal Predictions:")
print(final_pred)

accuracy = accuracy_score(y_test, final_pred)
precision = precision_score(y_test, final_pred)
recall = recall_score(y_test, final_pred)
f1 = f1_score(y_test, final_pred)
print("\n===== Final Model Evaluation =====")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)