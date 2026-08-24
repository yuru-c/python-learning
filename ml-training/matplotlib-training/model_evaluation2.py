import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    max_error, mean_absolute_error, mean_squared_error, r2_score
)

# data1
# data = {
#     "hours": [1, 2, 3, 4, 5, 6, 7, 8],
#     "score": [52, 58, 65, 71, 78, 84, 90, 95]
# }
# df = pd.DataFrame(data)
# x = df[["hours"]]
# y = df["score"]
# x_train, x_test, y_train, y_test = train_test_split(
#     x,y,
#     test_size=0.2, 
#     random_state=42
# )
# model = LinearRegression(fit_intercept=True)
# model.fit(x_train, y_train)
# y_pred = model.predict(x_test)
# print(y_test)
# print(y_pred)
# # residual = y_test - y_pred
# # print(residual)
# df["residual"] = y - model.predict(x)
# # Residual > 0 → Actual > Predicted → 模型低估
# # Residual < 0 → Actual < Predicted → 模型高估
# print(df)
# # print(x)
# # print(model.coef_)
# # print(model.intercept_)
# # print(model.predict(x))
# plt.scatter(x, df["residual"])
# plt.axhline(0)
# # 畫出 Residual = 0 的水平線
# plt.show()
# # 殘差在 0 附近隨機分布 沒有很明顯的曲線 => Linear Regression 很適合描述這組簡單資料
# # 如果殘差有明顯規律 模型可能還沒有抓到資料中的某些模式


# data2
data2 = {
    "x": [1, 2, 3, 4, 5, 6, 7, 8],
    "y": [2, 4, 9, 16, 25, 36, 49, 64]
}
df2 = pd.DataFrame(data2)
x2 = df2[["x"]]
y2 = df2["y"]
x2_train, x2_test, y2_train, y2_test = train_test_split(
    x2, y2, 
    test_size=0.2,
    random_state=42
)


# model = LinearRegression(fit_intercept=True)
# model.fit(x2_train, y2_train)
# # df2["residual2"] = y2 - model.predict(x2)
# # print(df2["residual2"])
# # plt.scatter(x2, df2["residual2"])
# # plt.axhline(0)
# # plt.show()
# y2_pred_linear = model.predict(x2)
# r2_linear = r2_score(y2, y2_pred_linear)
# print("Linear", r2_linear)


# Polynomial Regression y=ax²+bx+c
# Polynomial degree2
# poly = PolynomialFeatures(degree=2)
# x_poly = poly.fit_transform(x2)
# # 從訓練資料建立轉換規則 然後轉換
# # print(x_poly)
# model_poly = LinearRegression()
# model_poly.fit(x_poly, y2)
# # print("Intercept:", model_poly.intercept_)
# # print("Coefficients:", model_poly.coef_)
# y2_pred_poly = model_poly.predict(x_poly)
# df2["residual_poly"] = y2 - y2_pred_poly
# r2_poly = r2_score(y2, y2_pred_poly)
# print("Polynomial2", r2_poly)
# plt.scatter(x2, df2["residual_poly"])
# plt.axhline(0)
# plt.show()


# overfitting2
# poly = PolynomialFeatures(degree=2)
# x_train_poly = poly.fit_transform(x2_train)
# model_poly = LinearRegression()
# model_poly.fit(x_train_poly, y2_train)
# x_test_poly = poly.transform(x2_test)
# # 使用剛才學到的規則轉換測試資料
# y_test_pred_poly = model_poly.predict(x_test_poly)
# print(y2_test)
# print(y_test_pred_poly)
# r2_poly_test = r2_score(y2_test, y_test_pred_poly)
# print(r2_poly_test)


# Polynomial degree3
# poly3 = PolynomialFeatures(degree=3)
# x_poly3 = poly3.fit_transform(x2)
# model_poly3 = LinearRegression()
# model_poly3.fit(x_poly3, y2)
# y2_pred_poly3 = model_poly3.predict(x_poly3)
# r2_poly3 = r2_score(y2, y2_pred_poly3)
# print("Polynomial3", r2_poly3)


# overfitting3
# poly3 = PolynomialFeatures(degree=3)
# x_train_poly3 = poly3.fit_transform(x2_train)
# model_poly3 = LinearRegression()
# model_poly3.fit(x_train_poly3, y2_train)
# x_test_poly3 = poly3.transform(x2_test)
# y_test_pred_poly3 = model_poly3.predict(x_test_poly3)
# r2_poly3_test = r2_score(y2_test, y_test_pred_poly3)
# print(r2_poly3_test)


# # cross_val_score()
# #切資料 → 訓練 → 測試 → 換一批資料 → 再訓練 → 再測試 → ... → 得到多個分數
# model_cv = LinearRegression()
# scores = cross_val_score(
#     model_cv,
#     x2,
#     y2,
#     cv=4,
#     scoring="r2"
# )
# # cv=5 5-fold Cross-Validation
# # scoring="r2" 用 R² 評分
# print(scores)


# pipeline2
# model_poly_cv = Pipeline([
#     ("poly", PolynomialFeatures(degree=2)),
#     ("linear", LinearRegression())
# ])
# scores_poly = cross_val_score(
#     model_poly_cv,
#     x2,
#     y2,
#     cv=4,
#     scoring="r2"
# )
# print(scores_poly)
# mean_scores = scores_poly.mean()
# print(mean_scores)


# pipeline3
model_poly3_cv = Pipeline([
    ("poly", PolynomialFeatures(degree=3)),
    ("linear", LinearRegression())
])
scores_poly3 = cross_val_score(
    model_poly3_cv,
    x2,
    y2,
    cv=4,
    scoring="r2"
)
print(scores_poly3)
mean_scores_poly3 = scores_poly3.mean()
print(mean_scores_poly3)