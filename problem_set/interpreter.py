# import operator

# ops = {
#     "+":operator.add, 
#     "-":operator.sub, 
#     "*":operator.mul, 
#     "/":operator.truediv}

# x, y, z = input().split(" ")

# print(f"{ops[y](float(x), float(z)):.1f}")


x, y, z = input().split()

x = float(x)
z = float(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print(f"{result:.1f}")