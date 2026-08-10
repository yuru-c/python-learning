# import sys

# if len(sys.argv) == 1:
#     print("meow")
# # -n 次數
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow" \
#         "")
# else:
#     print("usage: meows.py")


# argparse argument parser 參數解析器
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
# _h == __help
args = parser.parse_args()


for _ in range(args.n):
    print("meow")

