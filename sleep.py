def main():
    n = int(input("What's n? "))
    # for i in range(n):
    #     print(sheep(i))

    for s in sheep(n):
        print(s)


def sheep(n):
    # return "🐏" * n

    """flock = []
    for i in range(n):
        flock.append("🐏" * i)
    return flock"""

    # yield 一次回傳一個值 (太多隻羊用return記憶體不夠)
    for i in range(n):
        yield "🐏" * i

if __name__ == "__main__":
    main()