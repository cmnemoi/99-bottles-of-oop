class Bottles:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, a: int, b: int) -> str:
        return "\n".join([self.verse(n) for n in range(a, b - 1, -1)])

    def verse(self, n: int) -> str:
        match n:
            case 0:
                return (
                    "No more bottles of beer on the wall, "
                    "no more bottles of beer.\n"
                    "Go to the store and buy some more, "
                    "99 bottles of beer on the wall.\n"
                )
            case _:
                return (
                    f"{n} {self._container(n)} of beer on the wall, "
                    f"{n} {self._container(n)} of beer.\n"
                    f"Take {self._pronoun(n)} down and pass it around, "
                    f"{self._quantity(n - 1)} {self._container(n - 1)} of beer on the wall.\n"
                )

    def _container(self, n: int) -> str:
        if n == 1:
            return "bottle"
        else:
            return "bottles"

    def _pronoun(self, n: int) -> str:
        if n == 1:
            return "it"
        else:
            return "one"

    def _quantity(self, n: int) -> str:
        if n == 0:
            return "no more"
        else:
            return str(n)
