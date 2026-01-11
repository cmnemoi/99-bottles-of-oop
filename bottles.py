class Bottle:
    def __init__(self, n: int) -> None:
        self.n = n if n >= 0 else 99

    def __str__(self) -> str:
        if self.n == 0:
            return "no more bottles"
        if self.n == 1:
            return f"{self.n} bottle"
        if self.n == 6:
            return "1 six-pack"

        return f"{self.n} bottles"

    def to_string(self) -> str:
        return self.__str__()

    def minus_one(self) -> "Bottle":
        return Bottle(self.n - 1)

    def act(self) -> str:
        if self.n == 0:
            return "Go to the store and buy some more, "
        elif self.n == 1:
            return "Take it down and pass it around, "

        return "Take one down and pass it around, "


class Bottles:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, a: int, b: int) -> str:
        return "\n".join(self.verse(n) for n in range(a, b - 1, -1))

    def verse(self, n: int) -> str:
        n_bottles = Bottle(n)
        return (
            f"{n_bottles.to_string().capitalize()} of beer on the wall, "
            f"{n_bottles} of beer.\n"
            f"{n_bottles.act()}"
            f"{n_bottles.minus_one()} of beer on the wall.\n"
        )
