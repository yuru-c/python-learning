import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit()

# if os.path.splitext(sys.argv[1])[1].lower() not in (".jpg", ".jpeg", ".png") or os.path.splitext(sys.argv[2])[1].lower() not in (".jpg", ".jpeg", ".png"):
#     print("Invalid input")
#     sys.exit()

# if os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
#     print("Input and output have different extensions")
#     sys.exit()

input_ext = os.path.splitext(sys.argv[1])[1].lower()
output_ext = os.path.splitext(sys.argv[2])[1].lower()

if input_ext not in (".jpg", ".jpeg", ".png") or \
    output_ext not in (".jpg", ".jpeg", ".png"):
    print("Invalid input")
    sys.exit()

if input_ext != output_ext:
    print("Input and output have different extensions")
    sys.exit()

try:
    shirt = Image.open("shirt.png")
    before = Image.open(sys.argv[1]) 

    # size = shirt.size
    # before = ImageOps.fit(before, size)

    before = ImageOps.fit(before, shirt.size)

    before.paste(shirt, shirt)
    before.save(sys.argv[2])
    
except FileNotFoundError:
    print("File does not exist")
    sys.exit()