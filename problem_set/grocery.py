groceries = []
while True:    
    try:
        items = input().strip().upper()        
        groceries.append(items)
    except EOFError:
        for item in sorted(set(groceries)):
            count = groceries.count(item)
            print(f"{count} {item}")
        break

        
    