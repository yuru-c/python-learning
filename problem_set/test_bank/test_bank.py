# import bank
from bank import value

# def test_lowercase():
#     assert value("hello") == "$0"
#     assert value("hello, world") == "$0"

# def test_uppercase():
#     assert value("HELLO") == "$0"

def test_hello():
    assert value("hello") == "$0"
    assert value("hello, world") == "$0"
    assert value("HELLO") == "$0"
    assert value("HELLO, WORLD") == "$0"
    assert value("   hello   ") == "$0"

def test_h():
    assert value("hi") == "$20"
    assert value("hey") == "$20"
    assert value("how are you") == "$20"

def test_other():
    assert value("good morning") == "$100"
    assert value("Good morning!") == "$100"
    assert value("what's up") == "$100"