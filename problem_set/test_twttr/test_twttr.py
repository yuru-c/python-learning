# import twttr
from twttr import shorten

# def main():
#     test_shorten()

# def test_shorten():
#     try:
#         assert shorten("twitter") == "twttr"
#     except AssertionError:
#         print("twitter is not twtter")
#     try:
#         assert shorten("apple") == "ppl"
#     except AssertionError:
#         print("twitter is not twtter")


# if __name__ == "__main__":
#     main()

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("apple") == "ppl"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("APPLE") == "PPL"

def test_no_vowels():
    assert shorten("rhythm") =="rhythm"

def test_all_vowels():
    assert shorten("aeiou") == ""

def test_numbers():
    assert shorten("12345") == "12345"

def test_punctauation():
    assert shorten("hello!") == "hll!"