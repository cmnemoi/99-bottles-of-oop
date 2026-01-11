from bottles import Bottle


def test_one_bottle() -> None:
    assert str(Bottle(1)) == "1 bottle"


def test_two_bottles() -> None:
    assert str(Bottle(2)) == "2 bottles"


def test_99_bottles() -> None:
    assert str(Bottle(99)) == "99 bottles"


def test_0_bottles() -> None:
    assert str(Bottle(0)) == "no more bottles"


def test_action_for_0_bottles() -> None:
    assert Bottle(0).act() == "Go to the store and buy some more, "


def test_action_for_1_bottle() -> None:
    assert Bottle(1).act() == "Take it down and pass it around, "


def test_action_for_more_bottles() -> None:
    assert Bottle(99).act() == "Take one down and pass it around, "
