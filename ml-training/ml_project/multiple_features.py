import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, root_mean_squared_error

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "sleep": [8, 7, 8, 6, 7, 6, 8, 7],
    "practice": [1, 1, 2, 2, 3, 3, 4, 4],
    "score": [51, 55, 62, 67, 75, 79, 88, 94]
}

df = pd.DataFrame(data)
# print(data)

x = df[["hours", "sleep", "practice"]]
y = df["score"]

# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)
# print(x_train)
# print(x_test)

model = LinearRegression()
# model.fit(x_train, y_train)
# print("Coefficients:", model.coef_)
# print("Intercept:", model.intercept_)

# y_pred = model.predict(x_test)
# print("Actual:")
# print(y_test)
# print("Predicted:")
# print(y_pred)
# mae = mean_absolute_error(y_test, y_pred)
# print("MAE:", mae)
# mse = mean_squared_error(y_test, y_pred)
# print("MSE:", mse)
# rmse = root_mean_squared_error(y_test, y_pred)
# print("RMSE:", rmse)
# r2 = r2_score(y_test, y_pred)
# print("R²:", r2)

# print(x.describe())

scores_linear = cross_val_score(
    model,
    x,
    y,
    cv=2,
    scoring="r2"
)
print("Mean R²(Linear):", scores_linear.mean())

# scaler = StandardScaler()
# # scaler.fit(x_train)
# # print("Mean:", scaler.mean_)
# # print("Scale:", scaler.scale_)
# # # z=(x-μ)/σ  μ = mean_ σ = scale_
# # x_train_scaled = scaler.transform(x_train)
# # # x_train_scaled = scaler.fit_transform(x_train)
# # print(x_train_scaled)
# # # hours 比平均值低約 1.56 個標準差 / sleep 比平均值高約 0.89 個標準差 / practice 比平均值低約 1.51 個標準差
# # # scaler.fit(x_test)不能寫 會讓 Test Data 的資訊跑進 preprocessing 破壞測試
# # # Training 和 Test 要使用相同標準
# # x_test_scaled = scaler.transform(x_test)
# # # x_test_scaled = scaler.transform(x_test)
# # print(x_test_scaled)

# # model_scaled = LinearRegression()
# # model_scaled.fit(x_train_scaled, y_train)
# # y_pred_scaled = model_scaled.predict(x_test_scaled)
# # print(y_pred_scaled)

model_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("linear", LinearRegression())
])
# model_pipeline.fit(x_train, y_train)
# y_pred_pipeline = model_pipeline.predict(x_test)
# print(y_pred_pipeline)
scores_cv2 = cross_val_score(
    model_pipeline,
    x,
    y,
    cv=2,
    scoring="r2"
)
print("Scores:", scores_cv2)
print("Mean R²(Standard+Linear):", scores_cv2.mean())
# # 對普通 Linear Regression，StandardScaler 通常不會改變模型的預測能力
# # StandardScaler 會影響 KNN / SVM / K-Means / Neural Network / Logistic Regression

# MinMaxScaler
# scaler_minmax = MinMaxScaler()
# scaler_minmax.fit(x_train)
# print("Min:", scaler_minmax.data_min_)
# print("Max:", scaler_minmax.data_max_)
# # x_scaled=(x-x_min)/(x_max-x_min)
# x_train_minmax = scaler_minmax.transform(x_train)
# print(x_train_minmax)
# x_test_minmax = scaler_minmax.transform(x_test)
# print(x_test_minmax)

model_minmax = Pipeline([
    ("scaler", MinMaxScaler()),
    ("linear", LinearRegression())
])
# model_minmax.fit(x_train, y_train)
# y_pred_minmax = model_minmax.predict(x_test)
# print(y_pred_minmax)
scores_minmax = cross_val_score(
    model_minmax,
    x,
    y,
    cv=2,
    scoring="r2"
)
print("Scores:", scores_minmax)
print("Mean R²(Minmax+Linear):", scores_minmax.mean())
# MinMaxScaler 常用在 KNN / Neural Network

# check
# print(model_pipeline)
# print()
# print(model_minmax)
# print(type(model_pipeline.named_steps["scaler"]))
# print(type(model_minmax.named_steps["scaler"]))
# print(type(model_pipeline.named_steps["linear"]))
# print(type(model_minmax.named_steps["linear"]))

linear_test = LinearRegression()

standard_test = Pipeline([
    ("scaler", StandardScaler()),
    ("linear", LinearRegression())
])

minmax_test = Pipeline([
    ("scaler", MinMaxScaler()),
    ("linear", LinearRegression())
])