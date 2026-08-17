from um import count

def test_um():
    assert count("um") == 1
    assert count("um?") == 1

def test_um_in_word():
    assert count("album") == 0
    assert count("yummy") == 0
    assert count("umbrella") == 0

def test_other():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("um123") == 0
    assert count("um_abc") == 0
    
    
