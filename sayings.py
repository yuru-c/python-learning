def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# 沒有下面這句 import後 結果會出現此處的main
# __name__ 其值為python自動設定
if __name__ == "__main__":
    main()