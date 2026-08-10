# MEOWS = 3

# for _ in range(MEOWS):
#     print("meow")

# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")


# cat = Cat()
# cat.meow()


# mypy 檢查型別錯誤
# n: int 提示 註解
def meow(n: int) -> str:
    """
    Meeow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return : A string of fn meows, one per line
    :rtype: str
    """
    # for _ in range(n):
    #     print("meow")
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")