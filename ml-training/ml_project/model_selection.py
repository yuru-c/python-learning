import pandas as pd
import numpy as np

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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
    x, y, test_size=0.2, random_state=42
)

model_linear = LinearRegression()
model_knn = KNeighborsRegressor(n_neighbors=1)
model_poly = Pipeline([
    ("poly", PolynomialFeatures(degree=2)),
    ("linear", LinearRegression())
])
models = {
    "Linear": model_linear,
    "KNN": model_knn,
    "Polynomial": model_poly
}
results = {}
for name, model in models.items():
    scores = cross_val_score(
        model,
        x, 
        y,
        cv=4,
        scoring="r2"
    )
    # print(name)
    # print("Scores:", scores)
    # print("Mean R²:", scores.mean())
    # print()
    results[name] = scores.mean()
print(results)
best_model = max(results, key=results.get)
# 在 dictionary 裡面找出 value 最大的 key
print("Best Model:", best_model)
print("Best CV R²:", results[best_model])
final_model = models[best_model]
final_model.fit(x_train, y_train)
# print("Final Model:", final_model)
y_final_pred = final_model.predict(x_test)
print("Actual:")
print(y_test)
print("Predicted:")
print(y_final_pred)
final_mae = mean_absolute_error(y_test, y_final_pred)
final_mse = mean_squared_error(y_test, y_final_pred)
final_rmse = np.sqrt(final_mse)
final_r2 = r2_score(y_test, y_final_pred)
print("MAE:", final_mae)
print("MSE:", final_mse)
print("RMSE:", final_rmse)
print("R²:", final_r2)