import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score

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
baseline_accuracy = accuracy_score(
    y_test, baseline_pred
)
print("\nBaseline Accuracy:")
print(baseline_accuracy)