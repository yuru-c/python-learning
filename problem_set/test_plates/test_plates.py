from plates import is_valid

# def test_len():
#     assert is_valid("abc123") == "Valid"
#     assert is_valid("a1") == "Invalid"

# def test_alpha():
#     assert is_valid("a123") == "Invalid"

# def test_num():
#     assert is_valid("abc!") == "Invalid"
#     assert is_valid("a0123") == "Invalid"

# def test_order():
#     assert is_valid("ab12ab") == "Invalid"

def test_length():
    assert is_valid("AB") == "Valid"
    assert is_valid("ABC123") == "Valid"
    assert is_valid("A") == "Invalid"
    assert is_valid("ABCDEFG") == "Invalid"

def test_first_two_letters():
    assert is_valid("AB12") == "Valid"
    assert is_valid("A123") == "Invalid"
    assert is_valid("123ABC") == "Invalid"

def test_characters():
    assert is_valid("ABC!") == "Invalid"
    assert is_valid("AB+12") == "Invalid"

def test_numbers():
    assert is_valid("AB12CD") == "Invalid"
    assert is_valid("AB05") == "Invalid"

def test_valid():
    assert is_valid("CS50") == "Valid"
    assert is_valid("HELLO") == "Valid"