'''string = input("Input: ")

print("Output: ", end="")

for s in string:
    # if s in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
    #     pass
    # else:
    #     print(s, end="")
    if s.lower() not in ("a", "e", "i", "o", "u"):
        print(s, end="")'''

string = input("Input: ")
vowels = "aeiou"
result = "".join(c for c in string if c.lower() not in vowels)
print("Output:", result)