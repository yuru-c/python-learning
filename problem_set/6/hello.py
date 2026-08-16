# name = input("what is your name?")

# remove whitspace from str
# name = name.strip()

# capitalize user's name
# name = name.capitalize()
# name = name.title()

# name = name.strip().title()

# name = input("what is your name?").strip().title()

# split user's name inton first name and last name
# first, last = name.split(" ")

# print(f"Hello, {name}")



def main():
    name = input("What;s your name? ")
    print(hello(name))


def hello(to="world"):
    # print("hello,", to)
    return f"hello, {to}"


if __name__ == "__main__":
    main()