class Bottles:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, a: int, b: int) -> str:
        return "\n".join([self.verse(i) for i in range(a, b - 1, -1)])

    def verse(self, n: int) -> str:
        bottle = "bottles" if n > 1 or n == 0 else "bottle"
        last_bottle = "bottles" if n - 1 > 1 or n <= 1 else "bottle"

        return (
            f"{self._formatted_n(n).capitalize()} {bottle} of beer on the wall, "
            f"{self._formatted_n(n)} {bottle} of beer.\n"
            + self._third_sentence(n)
            + f"{self._last_nb_bottles(n)} {last_bottle} of beer on the wall.\n"
        )

    def _formatted_n(self, n: int) -> str:
        if n == 0:
            return "no more"

        return str(n)

    def _last_nb_bottles(self, n: int) -> str:
        if n == 0:
            return "99"

        return "no more" if n - 1 < 1 else n - 1

    def _third_sentence(self, n: int) -> str:
        if n == 0:
            return "Go to the store and buy some more, "
        nb_bottles_to_take = "it" if n < 2 else "one"
        return f"Take {nb_bottles_to_take} down and pass it around, "
