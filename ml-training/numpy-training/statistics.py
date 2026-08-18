import numpy as np

scores = np.random.randint(0, 101, size=20)

print(scores)
print("Average:", scores.mean())
print("Maximum:", scores.max())
print("Minimum:", scores.min())
print("Standard deviation:", scores.std())
# >= 60 的學生有幾個
print("Passed:", np.sum(scores >= 60))
# >= 90 的學生有幾個
print("Excellent:", np.sum(scores >= 90))
# 不及格率
print("Fail rate:", np.mean(scores < 60))