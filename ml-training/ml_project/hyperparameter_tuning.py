import numpy as np
import pandas as pd

from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
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
    x, y,
    test_size=0.2,
    random_state=42
)


model_knn = KNeighborsRegressor()
param_grid = {
    "n_neighbors": [1, 2, 3, 4, 5]
}
# 告訴 GridSearchCV 幫我測這五種 K
grid_search = GridSearchCV(
    model_knn,
    param_grid,
    cv=4,
    scoring="r2"
)
grid_search.fit(x, y)
print("Best Parameters:", grid_search.best_params_)
print("Best CV R²:", grid_search.best_score_)


model_knn_standard = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsRegressor())
])
param_grid_standard = {
    "knn__n_neighbors": [1, 2, 3, 4, 5]
}
# 修改 Pipeline 裡面 knn 的 n_neighbors 要用_ _
grid_search_standard = GridSearchCV(
    model_knn_standard,
    param_grid_standard,
    cv=4,
    scoring="r2"
)
grid_search_standard.fit(x, y)
print("Best Parameters:", grid_search_standard.best_params_)
# best_params_ 第一名
print("Best CV R²:", grid_search_standard.best_score_)

results = pd.DataFrame(grid_search_standard.cv_results_)
# cv_results_ 所有資料的成績
print(results[
    [
        "param_knn__n_neighbors",
        "mean_test_score",
        "rank_test_score"
    ]
])


model_knn_minmax = Pipeline([
    ("scaler", MinMaxScaler()),
    ("knn", KNeighborsRegressor())
])
param_grid_minmax = {
    "knn__n_neighbors": [1, 2, 3, 4, 5]
}
grid_search_minmax = GridSearchCV(
    model_knn_minmax,
    param_grid_minmax,
    cv=4,
    scoring="r2"
)
grid_search_minmax.fit(x, y)
print("Best Parameters:", grid_search_minmax.best_params_)
print("Best CV R²:", grid_search_minmax.best_score_)


final_model = grid_search.best_estimator_
final_model.fit(x_train, y_train)
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