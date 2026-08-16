from numb3rs import validate

def test_valid():
    assert validate("1.1.1.1") == "True"
    assert validate("255.255.255.255") == "True"
    assert validate("0.0.0.0") == "True"
    assert validate("192.168.1.1") == "True"

def test_invalid():
    assert validate("256.256.256.256") == "False"
    assert validate("1000.1000.1000.1000") == "False"
    assert validate("1.1.1") == "False"
    assert validate("1.1.1.1.1") == "False"
    assert validate("01.01.01.01") == "False"
    assert validate("1.01.1.1") == "False"
    assert validate("cat") == "False"
    assert validate("1.a.1.1") == "False"
    assert validate("-.-.-.-") == "False"