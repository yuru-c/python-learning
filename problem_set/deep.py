fortytwo = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# if fortytwo == "42":
#     print("Yes")
# elif fortytwo == "forty-two":
#     print("Yes")
# elif fortytwo == "forty two":
#     print("Yes")
# else:
#     print("No")

# if fortytwo == "42" or "forty-two" or "forty two":
#     print("Yes")
# else:
#     print("No")

if fortytwo in ("42", "forty-two", "forty two"):
    print("Yes")
else:
    print("No")