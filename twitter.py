import re

url = input("URL: ").strip()

# 替代
# username = url.replace("https://twitter.com/", "")

# 移除前綴
# username = url.removeprefix("https://twitter.com/")

# re.split(pattern, string, mazsplit=0, flags=0)
# 搜尋同一圖案的多份複製 re.findall(pattern, string, flags=0)
# substitute 替代 re.sub(pattern, repl, string, count=0, flags=0)
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"Username:", matches.group(2))

# (?:) 不想被捕捉
if matches := re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/([a-z0-9_]+)$", url, re.IGNORECASE):
    # if matches.group(1) == "com":
    print(f"Username:", matches.group(1))