class Bottles:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, a: int, b: int) -> str:
        return "\n".join([self.verse(n) for n in range(a, b - 1, -1)])

    def verse(self, n: int) -> str:
        return (
            f"{self._quantity(n).capitalize()} {self._container(n)} of beer on the wall, "
            f"{self._quantity(n)} {self._container(n)} of beer.\n"
            f"{self._action(n)}, "
            f"{self._quantity(self._successor(n))} {self._container(self._successor(n))} of beer on the wall.\n"
        )

    def _container(self, n: int) -> str:
        if n == 1:
            return "bottle"

        return "bottles"

    def _pronoun(self, n: int) -> str:
        if n == 1:
            return "it"

        return "one"

    def _quantity(self, n: int) -> str:
        if n == 0:
            return "no more"

        return str(n)

    def _action(self, n: int) -> str:
        if n == 0:
            return "Go to the store and buy some more"

        return f"Take {self._pronoun(n)} down and pass it around"

    def _successor(self, n: int) -> int:
        if n == 0:
            return 99

        return n - 1
