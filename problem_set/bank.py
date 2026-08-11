greeting = input("Greeting: ").strip().lower()

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
    print("$100")