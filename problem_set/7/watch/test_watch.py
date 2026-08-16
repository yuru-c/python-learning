from watch import parse

def test_youtube():
    assert parse('<iframe src="https://www.youtube.com/embed/abc123"></iframe>') == "https://youtu.be/abc123"

def test_http():
    assert parse(
        '<iframe src="http://www.youtube.com/embed/abc123"></iframe>'
    ) == "https://youtu.be/abc123"

def test_invalid():
    assert parse("Hello") is None
    assert parse("https://google.com") is None