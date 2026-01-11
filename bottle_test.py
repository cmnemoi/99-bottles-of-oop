from bottles import Bottle


def test_one_bottle() -> None:
    assert str(Bottle(1)) == "1 bottle"


def test_two_bottles() -> None:
    assert str(Bottle(2)) == "2 bottles"


def test_99_bottles() -> None:
    assert str(Bottle(99)) == "99 bottles"


def test_0_bottles() -> None:
    assert str(Bottle(0)) == "no more bottles"
