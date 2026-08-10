# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")


"""def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

'list'
# coins = [100, 50, 25]
# print(total(coins[0], coins[1], coins[2]), "knuts")
# unpacking
# print(total(*coins), "knuts")

# print(total(galleons=100, sickles=50, knuts=25), "knuts")

'dic'
coins = {"galleons":100, "sickles":50, "knuts":25}
# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")
print(total(**coins), "knuts")"""

#kwargs 字典
def f(*args, **kwargs):
    # print("Positional:", args)
    print("Name:", kwargs)


# f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)


# def print(*object, sep=" ", end="\n", ...):