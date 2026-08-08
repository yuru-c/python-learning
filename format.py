import re

name = input("What's your name? ").strip()

"""if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")"""

'''matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)'''

# := 同時允許你指派一個從左到右的值 並提出布林問題 (海象操作員 walrus operator)
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")