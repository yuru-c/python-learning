import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "sleep": [6, 7, 8, 7, 6, 8, 7, 8],
    "practice": [1, 1, 2, 2, 2, 3, 4, 5],
    "score": [52, 55, 65, 71, 74, 84, 90, 95]
}

df = pd.DataFrame(data)

x = df[["hours", "sleep", "practice"]]
y = df["score"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

# print("X Train:")
# print(x_train)

# print("\nX Test:")
# print(x_test)

# print("\nY Train:")
# print(y_train)

# print("\nY Test:")
# print(y_test)

# linear
model_linear = LinearRegression()
model_linear.fit(x_train, y_train)
y_pred_linear = model_linear.predict(x_test)
# print("Actual:")
# print(y_test)
# print("Predicted:")
# print(y_pred_linear)
scores_linear = cross_val_score(
    model_linear,
    x,
    y,
    cv=4,
    scoring="r2"
)
print("Linear:", scores_linear)
print("Mean:", scores_linear.mean())



# standard
model_standard = Pipeline([
    ("scaler", StandardScaler()),
    ("linear", LinearRegression())
])
model_standard.fit(x_train, y_train)
y_pred_standard = model_standard.predict(x_test)
# print("Actual:")
# print(y_test)
# print("Predicted:")
# print(y_pred_standard)
scores_standard = cross_val_score(
    model_standard,
    x,
    y,
    cv=4,
    scoring="r2"
)
print("StandardScaler + Linear:", scores_standard)
print("Mean:", scores_standard.mean())


# minmax
model_minmax = Pipeline([
    ("scaler", MinMaxScaler()),
    ("linear", LinearRegression())
])
model_minmax.fit(x_train, y_train)
y_pred_minmax = model_minmax.predict(x_test)
# print("Actual:")
# print(y_test)
# print("Predicted:")
# print(y_pred_minmax)
scores_minmax = cross_val_score(
    model_minmax,
    x,
    y,
    cv=4,
    scoring="r2"
)
print("MinMaxScaler + Linear:", scores_minmax)
print("Mean:", scores_minmax.mean())