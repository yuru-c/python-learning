import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "score": [52, 58, 65, 71, 78, 84, 90, 95]
}

df = pd.DataFrame(data)

# print(df)

x = df[["hours"]]
y = df[["score"]]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, 
    test_size=0.2, 
    random_state=42
)
# random_state=42 每次執行時 切分結果固定 拿掉每次訓練和測試的資料可能不同

model = LinearRegression(fit_intercept=True)
# fit_intercept=True 讓線性回歸模型自己學習截距
# y = ax + b   a → slope（斜率）b → intercept（截距）
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(y_test)
print(y_pred)
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
# y = ax + b : a = model.coef_ / b = model.intercept_
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R² Score:", r2)

plt.scatter(data["hours"], data["score"])
y_line = model.predict(x)
plt.plot(data["hours"], y_line)
plt.show()
