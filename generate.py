"""from random import choice

coin = choice(["heads","tails"])
print(coin)"""


import random

"""coin = random.choice(["heads","tails"])
print(coin)
"""

# 隨機數字 randint
"""number = random.randint(1, 10)
print(number)"""

# 洗牌 shuffle
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

