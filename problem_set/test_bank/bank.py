# 原本版本
'''greeting = input("Greeting: ").strip().lower()

# if "hello" in greeting:
#     print("$0")
# elif greeting[0] == "h":
#     print("$20")
# else:
#     print("$100")

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")'''

# 為test_bank修改
def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()