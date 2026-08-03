"""x = float(input("what's x? "))
y = float(input("what's y? "))

# z = round(x + y)
# 三位數分號 1,000
# print(f"{z:,}")

# z = round(x / y, 2)

z = x / y

print(f"{z:.2f}")"""

def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))

def square(n):
    # return n * n
    return pow(n, 2)

main()