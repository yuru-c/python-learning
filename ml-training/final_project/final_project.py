import pandas as pd
import matplotlib.pyplot as plt

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
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix,
    roc_curve, roc_auc_score
)

# 1.Project Goal 能不能利用學生的背景資料與前期成績，預測學生最後是否會通過

# 2.Dataset UCI Student Performance Dataset 的 student-mat.csv
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

# 3.Data Preprocessing 資料裡面同時有數字和文字
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

# 4.Models
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

# 5.Final Model
# 6.Final Evaluation
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

# 7.Confusion Matrix
cm = confusion_matrix(y_test, final_pred)
print("\n===== Confusion Matrix =====")
print(cm)

final_proba = final_model.predict_proba(X_test)[:, 1]
print("\n===== Predicted Probabilities =====")
print(final_proba)

fpr, tpr, thresholds = roc_curve(y_test, final_proba) 
print("\n===== ROC Data =====")
# 實際是 0 的人，有多少被錯誤預測成 1
print("FPR:")
print(fpr)
# 實際是 1 的人，有多少成功被預測成 1 =Recall
print("TPR:")
print(tpr)
print("Thresholds:")
print(thresholds)

# 8.ROC-AUC
auc = roc_auc_score(y_test, final_proba)
print("\nROC-AUC:")
print(auc)

plt.figure(figsize=(6, 6))
plt.plot(fpr, tpr, label=f"Logistic Regression (AUC = {auc:.3f})")
plt.plot([0, 1], [0, 1], linestyle="--", label="Random")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

# 9.Feature Importance
feature_names = (final_model.named_steps["preprocessor"].get_feature_names_out())
# 從 Pipeline 裡找到 preprocessing，告訴我資料經過轉換後有哪些 feature

coefficients = final_model.named_steps["model"].coef_[0]
# 從 Pipeline 裡找到 Logistic Regression，把它學到的每個 feature 的 coefficient 拿出來

feature_importance = pd.DataFrame({
    "feature": feature_names,
    "coefficient": coefficients,
    "importance": abs(coefficients)
})
feature_importance = feature_importance.sort_values(
    "importance",
    ascending=False
)
print("\n===== Feature Importance =====")
print(feature_importance.head(15))

# 10.Error Analysis
errors = X_test.copy()
errors["actual"] = y_test
errors["predicted"] = final_pred
errors = errors[errors["actual"] != errors["predicted"]]
print("\n===== Error Analysis =====")
print(errors)

fp_errors = errors[(errors["actual"] == 0) & (errors["predicted"] == 1)]
fn_errors = errors[(errors["actual"] == 1) & (errors["predicted"] == 0)]
print("\n===== False Positives =====")
print(fp_errors)
print("\n===== False Negatives =====")
print(fn_errors)
important_columns = [
    "G1",
    "G2",
    "age",
    "Walc",
    "famrel",
    "failures"
]
print("\n===== Important Features of Errors =====")
print(errors[important_columns + ["actual", "predicted"]])

# 11.Project Limitations ①Dataset不大 ②Dataset有特定背景 ③我們使用了G1/G2(已經知道前期成績後，預測最後是否通過)

# 12.Project Conclusion
"""我們使用 UCI Student Performance Dataset 建立學生最終通過與否的二元分類模型。經過資料探索、Target Engineering、One-Hot Encoding、Scaling、Pipeline、Train/Test Split、Cross-Validation 與 Hyperparameter Tuning 後，比較 Baseline、Logistic Regression 與 KNN。最終選擇 Logistic Regression 作為 Final Model，於測試集得到 84.81% Accuracy、93.62% Precision、83.02% Recall、88.00% F1，以及 93.47% ROC-AUC。Feature analysis 顯示 G1 與 G2 是模型中最具影響力的特徵，而 Error Analysis 顯示模型主要錯誤來自 False Negative。整體而言，Logistic Regression 在此 Dataset 上展現良好的分類能力，但由於資料量、資料來源與測試集規模有限，結果不應直接視為模型在其他學生群體上的泛化表現。"""