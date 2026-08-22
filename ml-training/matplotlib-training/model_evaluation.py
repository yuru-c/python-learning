import pandas as pd
import math
from sklearn.metrics import r2_score

data = {
    "actual": [85, 90, 78, 92, 70, 88, 95, 60],
    "predicted": [82, 88, 80, 89, 72, 85, 91, 65]
}

df = pd.DataFrame(data)

df["error"] = df["actual"]-df["predicted"]
df["absolute_error"] = abs(df["actual"]-df["predicted"])
# MAE = df["absolute_error"].sum() / len(df["absolute_error"])
MAE = df["absolute_error"].mean()
print(MAE)
# MAE = mean absolute error 平均錯多少？

df["squared_error"] = df["error"].pow(2)
MSE = df["squared_error"].mean()
print(MSE)
# MSE = mean squared error 會放大較大的誤差 對大誤差特別敏感 大錯誤有多嚴重？
RMSE = math.sqrt(MSE)
print(RMSE)
# RMSE = root mean squared error 大錯誤有多嚴重，而且回到原本單位？


# R² = 1 - SSE(模型還剩多少錯誤) / SST(資料本身有多少變化) 模型抓住資料變化的程度如何？
# R² = 1 模型完全抓住資料的變化
# R² = 0 模型跟「直接猜平均值」差不多
# R² < 0 模型甚至比「直接猜平均值」還糟
# R² = 0.8 不代表「預測準確率 80%」而是模型解釋了資料中約 80% 的變化 約 20% 的變化沒有被模型解釋
mean_actual = df["actual"].mean()
# SST = Σ(actual - mean_actual)²
SST = (df["actual"]-mean_actual).pow(2).sum()
SSE = df["squared_error"].sum()
R2 = 1 - (SSE / SST)
print(R2)
r2 = r2_score(df["actual"], df["predicted"])
print(r2)
# print(df)