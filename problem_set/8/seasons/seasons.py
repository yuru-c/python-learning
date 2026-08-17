from datetime import date, datetime
import inflect
# import datetime as dt
# import re
# import operator


def main():
    print(convert(input("Date of Birth: ")))

def convert(s):
    # if matches := re.search(r"\d\d\d\d-\d\d-\d\d", s):
    #     birthday = datetime.strptime(s, "%Y-%m-%d").date().toordinal()
    #     today = date.today().toordinal()
    #     p = inflect.engine()
    #     minutes = p.number_to_words(operator.__sub__(today, birthday) * 24 * 60).capitalize()      
    #     return f"{minutes} minutes"
    # else:
    #     return "Invalid date"

    try:
        birthday = datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return "Invalid date"

    today = date.today()
    minutes = (today - birthday).days * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(minutes).capitalize()

    return f"{words} minutes"

if __name__ == "__main__":
    main()