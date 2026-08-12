'''d = 50
print("Amount Due:", d)

while d != 0:
    insert = int(input("Insert Coin: "))
    # if insert == 25:
    #     d -= 25
    # elif insert == 10:
    #     d -= 10
    # elif insert == 5:
    #     d -= 5
    if insert in [25, 10, 5]:
        d -= insert
    if d == 0:
        print("Change Owed: 0")
    else:
        print("Amout Due: ", d)'''


amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))

    if coin in (25, 10, 5):
            amount_due -= coin

print(f"Change Owed: {abs(amount_due)}")
