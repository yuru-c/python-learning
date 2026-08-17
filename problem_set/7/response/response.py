from validator_collection import validators, errors

def main():
    print(response(input("What's your email address? ")))

def response(a):
    try:
        validators.email(a.strip())
        return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"

if __name__ == "__main__":
    main()