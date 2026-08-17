from seasons import convert

def test_valid():
    assert convert("2026-08-16") == "One thousand, four hundred and forty minutes"
    assert convert("2025-08-17") == "Five hundred and twenty-five thousand, six hundred minutes"
    assert convert("2024-08-17") == "One million, fifty-one thousand, two hundred minutes"

def test_invalid():
    assert convert("January 1, 1999") == "Invalid date"
    assert convert("hello") == "Invalid date"
    assert convert("2026-02-30") == "Invalid date"