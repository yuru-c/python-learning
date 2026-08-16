import sys

# if len(sys.argv) <= 1:
#     print("Too few command-line arguments")
#     sys.exit()
# elif len(sys.argv) >= 3:
#     print("Too many command-line argumetns")
#     sys.exit()
# elif len(sys.argv) == 2:
#     if not sys.argv[1].endswith(".py"):
#         print("Not a Python file")
#         sys.exit()
#     else:
#         try:
#             with open(sys.argv[1]) as file:
#                 loc = 0
#                 for line in file:
#                     line = line.strip()

#                     if line == "":
#                         continue

#                     if line.startswith("#"):
#                         continue

#                     loc += 1
#             print(loc)
#         except FileNotFoundError:
#             print("File does not exist")
#             pass


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit()

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()

if not sys.argv[1].endswith(".py"):
    print("Not a Python file")
    sys.exit()

try:
    with open(sys.argv[1]) as file:
        loc = 0

        for line in file:
            line = line.strip()

            if line == "" or line.startswith("#"):
                continue

            loc += 1

    print(loc)

except FileNotFoundError:
    print("File does not exist")
    sys.exit()