import sys

# sys.argv[0] 是程式名稱
# 沒有在終端機輸入名字 會出現 IndexError: list index out of range

"""try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")"""

"""# check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
'''else:'''

#print name tags 這樣子會出現 IndexError: list index out of range
print("hello, my name is", sys.argv[1])"""

# if len(sys.argv) < 2:
#     # 乾脆退出
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# #print name tags
# print("hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)