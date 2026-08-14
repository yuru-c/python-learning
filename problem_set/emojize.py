import emoji

# print(f"Output: {emoji.emojize(input('Input: ').strip().lower(), language='alias')}")

text = input("Input: ").strip().lower()
print(f"Output: {emoji.emojize(text, language='alias')}")