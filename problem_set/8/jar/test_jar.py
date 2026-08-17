from jar import Jar
import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_deposit():
    # jar = Jar(10)
    # jar.deposit(3)
    # assert jar.capacity == 10
    # assert jar.size == 3

    # jar = Jar(10)
    # jar.deposit(10)
    # assert jar.capacity == 10
    # assert jar.size == 10

    jar = Jar(10)

    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(7)
    assert jar.size == 10

def test_deposit_error():
    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.deposit(6)


def test_withdraw():
    # jar = Jar(10)
    # jar.deposit(5)
    # jar.withdraw(2)
    # assert jar.size == 3

    # jar = Jar(10)
    # jar.deposit(5)
    # jar.withdraw(5)
    # assert jar.size == 0

    jar = Jar(10)
    jar.deposit(5)

    jar.withdraw(2)
    assert jar.size == 3

    jar.withdraw(3)
    assert jar.size == 0


def test_withdraw_error():
    jar = Jar(10)
    jar.deposit(2)

    with pytest.raises(ValueError):        
        jar.withdraw(3)

    # with pytest.raises(ValueError):
    #     jar = Jar(10)
    #     jar.deposit(2)
    #     jar.withdraw(11)


def test_capacity_invalid():
    with pytest.raises(ValueError):
        # jar = Jar(0)
        Jar(0)
    with pytest.raises(ValueError):
        # jar = Jar(-1)
        Jar(-1)


def test_str():
    jar = Jar(10)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"



def test_negative_deposit():
    jar = Jar(10)

    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_negative_withdraw():
    jar = Jar(10)
    jar.deposit(5)

    with pytest.raises(ValueError):
        jar.withdraw(-1)