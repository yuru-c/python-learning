# import numpy as np

'''scores = np.array([80, 90, 70, 85])

print(scores)
print(type(scores))
print(scores.shape)
print(scores[0])
# print(scores[len(scores) - 1])
print(scores[-1])'''

'''scores = np.array([
    [80, 90, 70],
    [60, 75, 85], 
    [90, 95, 88]
    ])

print(scores.shape)
print(scores[0])
print(scores[1])
print(scores[0, 1])'''

'''scores = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [90, 95, 88]
])

print(scores[:, 0])
print(scores[:, 1])
print(scores[:, 2])'''

'''scores = np.array([60, 70, 80, 90])

print(scores + 5)
print(scores * 2)
print(scores / 10)'''


import numpy as np

'''scores = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [90, 95, 88],
    [70, 65, 72]
])

print(scores.shape)
print(scores[0])
print(scores[:, 0])
print(scores + 5)
# print(scores.sum() / (scores.shape[0] * scores.shape[1]))
print(scores.mean())
# print(scores.sum(axis=1) / scores.shape[1])
print(scores.mean(axis=1))
# print(scores.sum(axis=0) / scores.shape[0])
print(scores.mean(axis=0))
print(scores.max())
print(scores.min())'''

'''scores = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [90, 95, 88],
    [70, 65, 72]
])

print(scores + 5)
print(scores * 1.1)
print(scores[scores >= 80])
print(np.all(scores >= 70, axis=1))
print(np.any(scores >= 90, axis=1))
print(scores[scores < 70])
print(scores[np.any(scores >= 90, axis=1)])'''

numbers = np.arange(1, 13)
matrix = numbers.reshape(3, 4)

print(matrix)
print(matrix.shape)
print(matrix.sum(axis=1))
print(matrix.sum(axis=0))
print(matrix.mean(axis=1))
print(matrix.mean(axis=0))
print(matrix.max())