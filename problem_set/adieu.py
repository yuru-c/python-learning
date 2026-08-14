import inflect

p = inflect.engine()
names=[]
while True:
    try:
        name = input("Name: ").strip()
        names.append(name)
    except EOFError:        
        # print(f"Adieu, adieu, to {p.join(names)}")
        break

# EOF負責結束輸入 while結束後再統一輸出
print(f"Adieu, adieu, to {p.join(names)}")