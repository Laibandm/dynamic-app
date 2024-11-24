import app

def test_add():
    assert app.add(3, 2) == 5
    assert app.add(-1, 1) == 0

def test_subtract():
    assert app.subtract(3, 2) == 1
    assert app.subtract(5, 7) == -2
