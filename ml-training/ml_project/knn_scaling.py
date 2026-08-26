import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor

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

# KNN
model_knn = KNeighborsRegressor(n_neighbors=3)
# 會找距離最近的 3 個 Training Samples 再利用它們的分數來進行預測
# prediction=(y1+y2+y3)/3
# KNN最常用的是Euclidean Distance（歐幾里得距離） → Scaling 可能改變距離
# d(A,B)=sqrt{(hours1-hours2)^2+(sleep1-sleep2)^2+(practice1-practice2)^2}
model_knn.fit(x_train, y_train)
y_pred_knn = model_knn.predict(x_test)
print("Actual:")
print(y_test)
print("Predicted:")
print(y_pred_knn)


# StandardScaler + KNN
model_knn_standard = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsRegressor(n_neighbors=3))
])
model_knn_standard.fit(x_train, y_train)
y_pred_knn_standard = model_knn_standard.predict(x_test)
print("Actual:")
print(y_test)
print("Predicted:")
print(y_pred_knn_standard)


# KNN評估
mae_knn = mean_absolute_error(y_test, y_pred_knn)
mse_knn = mean_squared_error(y_test, y_pred_knn)
rmse_knn = np.sqrt(mse_knn)
r2_knn = r2_score(y_test, y_pred_knn)
print("KNN")
print("MAE:", mae_knn)
print("MSE:", mse_knn)
print("RMSE:", rmse_knn)
print("R²:", r2_knn)
mae_knn_standard = mean_absolute_error(y_test, y_pred_knn_standard)
mse_knn_standard = mean_squared_error(y_test, y_pred_knn_standard)
rmse_knn_standard = np.sqrt(mse_knn_standard)
r2_knn_standard = r2_score(y_test, y_pred_knn_standard)
print("\nStandardScaler + KNN")
print("MAE:", mae_knn_standard)
print("MSE:", mse_knn_standard)
print("RMSE:", rmse_knn_standard)
print("R²:", r2_knn_standard)

scores_knn = cross_val_score(
    model_knn, x, y, cv=4, scoring="r2"
)
scores_knn_standard = cross_val_score(
    model_knn_standard, x, y, cv=4, scoring="r2"
)
print("KNN:", scores_knn)
print("Mean KNN:", scores_knn.mean())
print("StandardScaler + KNN:", scores_knn_standard)
print("Mean StandardScaler + KNN:", scores_knn_standard.mean())

best_k = None
best_score_k = -float("inf")
for k in range(1,6):
    model_knn_k = KNeighborsRegressor(n_neighbors=k)
    scores_knn_k = cross_val_score(
        model_knn_k, x, y, cv=4, scoring="r2"
    )
    mean_score = scores_knn_k.mean()
    print("K:", k)
    print("Scores:", scores_knn_k)
    print("Mean R²:", mean_score)
    if mean_score > best_score_k:
        best_score_k = mean_score
        best_k = k
print("Best K:", best_k)
print("Best CV R²:", best_score_k)

best_k_standard = None
best_score_standard = -float("inf")
for k in range(1,6):
    model_knn_standard_k = Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsRegressor(n_neighbors=k))
    ])    
    scores_knn_standard_k = cross_val_score(
        model_knn_standard_k, x, y, cv=4, scoring="r2"
    )
    mean_score = scores_knn_standard_k.mean()
    print("K:", k)
    print("Scores:", scores_knn_standard_k)
    print("Mean R²:", mean_score)
    if mean_score > best_score_standard:
        best_score_standard = mean_score
        best_k_standard = k
print("Best K StandardScaler:", best_k_standard)
print("Best CV R² StandardScaler:", best_score_standard)