import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

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
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
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