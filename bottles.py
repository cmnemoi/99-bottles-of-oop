class Bottle:
    def __init__(self, n: int) -> None:
        self.n = n if n >= 0 else 99

    def __str__(self) -> str:
        if self.n == 0:
            return "no more bottles"
        if self.n == 1:
            return f"{self.n} bottle"
        else:
            return f"{self.n} bottles"

    def to_string(self) -> str:
        return self.__str__()

    def remove_one(self) -> "Bottle":
        return Bottle(self.n - 1)


class Bottles:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, a: int, b: int) -> str:
        return "\n".join([self.verse(n) for n in range(a, b - 1, -1)])

    def verse(self, n: int) -> str:
        bottles = Bottle(n)
        match n:
            case 1:
                return (
                    f"{bottles} of beer on the wall, "
                    f"{bottles} of beer.\n"
                    "Take it down and pass it around, "
                    f"{bottles.remove_one()} of beer on the wall.\n"
                )
            case 0:
                return (
                    f"{bottles.to_string().capitalize()} of beer on the wall, "
                    f"{bottles} of beer.\n"
                    "Go to the store and buy some more, "
                    f"{bottles.remove_one()} of beer on the wall.\n"
                )
            case _:
                return (
                    f"{Bottle(n)} of beer on the wall, "
                    f"{Bottle(n)} of beer.\n"
                    "Take one down and pass it around, "
                    f"{bottles.remove_one()} of beer on the wall.\n"
                )
