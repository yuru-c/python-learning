import random

# while True:
#     try:
#         level = int(input("Level: "))
#         number = random.randint(1, level)
#         break
#     except (ValueError, TypeError):
#         pass

# while True:
#     try:
#         guess = int(input("Guess: "))
#         if guess == number:
#             print("Just right!")
#             break
#         elif guess > number:
#             print("Too large!")
#         elif number > guess >= 1:
#             print("Too small!")

#     except (ValueError, TypeError):
#         pass

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess == number:
            print("Just right!")
            break
        elif guess > number:
            print("Too large!")
        else:
            print("Too small!")

    except ValueError:
        pass