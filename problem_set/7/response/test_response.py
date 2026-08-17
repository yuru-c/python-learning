from response import response

def test_valid():
    assert response("malan@harvard.edu") == "Valid"
    assert response("  malan@harvard.edu  ") == "Valid"
    assert response("user@gmail.com") == "Valid"

def test_invalid():
    assert response("malan") == "Invalid"
    assert response("malan@@@harvard.edu") == "Invalid"
    assert response("malan@harvard..edu") == "Invalid"
    assert response("malan@harvard") == "Invalid"