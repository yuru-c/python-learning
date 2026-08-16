import sys
import csv

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit()

# table = []
# try:
#     with open(sys.argv[1]) as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             name = row["name"]
#             house = row["house"]
#             last, first = name.split(", ")
#             table.append({"first": first, "last": last, "house": house})        
# except FileNotFoundError:
#     print("File does not exist")
#     sys.exit()

# with open(sys.argv[2], "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["first", "last", "house"])
#     for row in table:
#         writer.writerow([row["first"], row["last"], row["house"]])


try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)

        with open(sys.argv[2], "w", newline="") as output:
            writer = csv.DictWriter(
                output, fieldnames=["first", "last", "house"]
            )

            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")

                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })

except FileNotFoundError:
    print("File does not exist")
    sys.exit()