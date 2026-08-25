import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, root_mean_squared_error

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "sleep": [8, 7, 8, 6, 7, 6, 8, 7],
    "practice": [1, 1, 2, 2, 3, 3, 4, 4],
    "score": [51, 55, 62, 67, 75, 79, 88, 94]
}

df = pd.DataFrame(data)
print(data)

x = df[["hours", "sleep", "practice"]]
y = df["score"]

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)
print(x_train)
print(x_test)

model = LinearRegression()
model.fit(x_train, y_train)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

y_pred = model.predict(x_test)
print("Actual:")
print(y_test)
print("Predicted:")
print(y_pred)
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)
rmse = root_mean_squared_error(y_test, y_pred)
print("RMSE:", rmse)
r2 = r2_score(y_test, y_pred)
print("R²:", r2)

print(x.describe())

scaler = StandardScaler()
scaler.fit(x_train)
print("Mean:", scaler.mean_)
print("Scale:", scaler.scale_)
# z=(x-μ)/σ  μ = mean_ σ = scale_
x_train_scaled = scaler.transform(x_train)
# x_train_scaled = scaler.fit_transform(x_train)
print(x_train_scaled)
# hours 比平均值低約 1.56 個標準差 / sleep 比平均值高約 0.89 個標準差 / practice 比平均值低約 1.51 個標準差
# scaler.fit(x_test)不能寫 會讓 Test Data 的資訊跑進 preprocessing 破壞測試
# Training 和 Test 要使用相同標準
x_test_scaled = scaler.transform(x_test)
# x_test_scaled = scaler.transform(x_test)
print(x_test_scaled)

model_scaled = LinearRegression()
model_scaled.fit(x_train_scaled, y_train)
y_pred_scaled = model_scaled.predict(x_test_scaled)
print(y_pred_scaled)