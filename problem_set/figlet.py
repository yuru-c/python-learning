from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

# if len(sys.argv) < 2: 
#     f = random.choice(figlet.getFonts())
#     figlet.setFont(font=f)
#     s = input("Input: ").strip()   
#     print(figlet.renderText(s))
# else:
#     if sys.argv[1] == "-f" or sys.argv[1] == "--font":
#         f = font=sys.argv[2]
#         if f not in figlet.getFonts():
#             print("Invalid usage")
#         else:
#             s = input("Input: ").strip()
#             figlet.setFont(font=sys.argv[2])
#             print(figlet.renderText(s))
#     else:
#         print("Invalid usage")

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())

elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    font = sys.argv[2]

    if font not in figlet.getFonts():
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

figlet.setFont(font=font)

text = input("Input: ")
print(figlet.renderText(text))