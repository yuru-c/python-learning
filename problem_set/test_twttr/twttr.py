'''string = input("Input: ")

print("Output: ", end="")

for s in string:
    # if s in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
    #     pass
    # else:
    #     print(s, end="")
    if s.lower() not in ("a", "e", "i", "o", "u"):
        print(s, end="")'''


# 原本版本
'''string = input("Input: ")
vowels = "aeiou"
result = "".join(c for c in string if c.lower() not in vowels)
print("Output:", result)'''


# 為test_twttr修改
def main():
    text = input("Input:")
    print(f"Output: {shorten(text)}")


def shorten(word):
    vowels = "aeiou"
    return "".join(w for w in word if w.lower() not in vowels)


if __name__ == "__main__":
    main()