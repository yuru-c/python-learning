import re

def main():
    print(count(input("Text: ")))

def count(s):
    # matches = re.findall(r"(?:[^a-zA-Z]|^)um(?:[^a-zA-Z]|$)", s)
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    # \b word boundary（單字邊界）
    return len(matches)
    
if __name__ == "__main__":
    main()