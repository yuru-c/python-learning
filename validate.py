# email valid 1
'''email = input("What's your email? ").strip()
# strip 移除特定字元 (預設空白)

"""if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")"""

username, domain = email.split("@")

# if (username) and ("." in domain):
if (username) and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invelid")'''

# re library (regular expression)
import re

email = input("What's your email? ").strip()
# 正規表示式（Regular Expression，Regex）
# . any character except a newlline 任意一個字元（不包含換行 \n）a.c abc、a1c、a-c
# * 0 or more repetitions 前面的模式出現 0 次或以上 ab*c ac、abc、abbc、abbbc
# + 1 or more repetitions 前面的模式出現 1 次或以上 ab+c abc、abbc，不能匹配 ac
# ? 0 or 1 repetition 前面的模式出現 0 次或 1 次 ab?c ac、abc，不能匹配 abbc
# {m} m repetitions 前面的模式剛好出現 m 次 a{3} aaa
# {m,n} m-n repetitions 前面的模式出現 m 到 n 次 a{2,4} aa、aaa、aaaa
# ^ matches the start of the string 比對字串開頭
# $ matches the end of the string or just before the newline at ehe end of the string 比對字串結尾
# [] set of characters 符合其中任意一個字元
# [^] complementing the set 補集（Complement）
# \d=[0-9] \D=[^0-9] decimal digit
# \w=[A-Za-z0-9_] \W=[^A-Za-z0-9_] word character
# \s=空白字元（空格、Tab、換行等）\S=非空白字元 whitespace characters
# A|B or () group (?:) non-capturing version
# re.IGNORECASE re.MULTLINE re.DOTALL

# "..*@..*" = ".+@.+"
# r"^.+@.+\.edu$"
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invelid")