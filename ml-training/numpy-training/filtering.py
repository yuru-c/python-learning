import numpy as np

'''scores = np.array([45, 67, 82, 91, 56, 73, 88, 39, 100, 64])

print(scores[scores >= 60])
print(scores[scores < 60])
print(scores[scores >= 90])
print(np.sum(scores >= 60))
print(np.sum(scores >= 90))
print(scores[scores < 60] + 10)

# array = scores[(scores >= 60) & (scores < 90)]
# print(array)
passing_scores = scores[(scores >= 60) & (scores < 90)]
print(passing_scores)'''

'''scores = np.array([45, 67, 82, 91, 56])
print(scores)
print(np.where(scores < 60, 60, scores))'''

scores = np.array([45, 67, 82, 91, 56, 73, 38, 100])
print(scores)
print(np.where(scores < 60, 60, scores))
print(np.where(scores >= 90, 100, scores))
# print(np.where(scores < 60, "Fail",
#                np.where(scores < 80, "Pass",
#                         np.where(scores < 90, "Good",
#                                  np.where(scores >= 90, "Excellent", "")))))
# print(np.where(
#     scores < 60, 
#     "Fail",
#     np.where(
#         scores < 80, 
#         "Pass",
#         np.where(
#             scores < 90, 
#             "Good",
#             "Excellent"
#         )
#     )
# ))


conditions = [
    scores < 60,
    scores < 70,
    scores < 80,
    scores < 90,
    # scores >= 90
]

choices = [
    "F",
    "D",
    "C",
    "B",
    # "A"
]

# result = np.select(conditions, choices, default="Unknown")
result = np.select(conditions, choices, default="A")
print(result)