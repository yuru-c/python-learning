def main():
    # yell(["This", "is", "CS50"])
    yell("This", "is", "CS50")


#def yell(words):
def yell(*words):
    # print(phrase.upper())

    '''uppercased = []
    for word in words:
       uppercased.append(word.upper())'''

    # map 映射
    # uppercased = map(str.upper, words)

    uppercased = [word.upper() for word in words]

    print(*uppercased)


if __name__ == "__main__":
    main()