'''camel = input("camelCase: ")
snake = []
for c in camel:
    if c.isupper():    
        # c = c.rjust(2, "_")
        c = "_" + c
    snake.append(c.lower())

# print("snake_case: ", end="")
# for s in snake:
#     print(s, end="")

print(f"snake_case: {"".join(snake)}" )'''

camel = input("camelCase: ")
print("snake_case: ", end="")
for c in camel:
    if c.isupper():
        print("_", end="")
    print(c.lower(), end="")

print()