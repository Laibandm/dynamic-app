import pytest
import app

def test_add():
    assert app.add(2, 3) == 5
    assert app.add(-1, 1) == 0
    assert app.add(0, 0) == 0

def test_subtract():
    assert app.subtract(5, 3) == 2
    assert app.subtract(0, 3) == -3
    assert app.subtract(-3, -3) == 0

def test_multiply():
    assert app.multiply(2, 3) == 6
    assert app.multiply(-1, 3) == -3
    assert app.multiply(0, 5) == 0

def test_divide():
    assert app.divide(6, 3) == 2
    assert app.divide(-6, 2) == -3
    assert app.divide(5, 2) == 2.5

    with pytest.raises(ValueError):
        app.divide(5, 0)
