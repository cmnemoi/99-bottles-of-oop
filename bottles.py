class Bottles:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, a: int, b: int) -> str:
        return "\n".join([self.verse(n) for n in range(a, b - 1, -1)])

    def verse(self, n: int) -> str:
        return (
            f"{n if n > 0 else 'no more'.capitalize()} {'bottle' if n == 1 else 'bottles'} of beer on the wall, "
            f"{n if n > 0 else 'no more'} {'bottle' if n == 1 else 'bottles'} of beer.\n"
            + self._third_sentence(n)
            + f"{self._last_nb_bottles(n)} {'bottle' if n - 1 == 1 else 'bottles'} of beer on the wall.\n"
        )

    def _last_nb_bottles(self, n: int) -> str:
        if n == 0:
            return "99"

        return "no more" if n < 2 else str(n - 1)

    def _third_sentence(self, n: int) -> str:
        if n == 0:
            return "Go to the store and buy some more, "

        return f"Take {'it' if n <= 1 else 'one'} down and pass it around, "
