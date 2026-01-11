class Bottles:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, a: int, b: int) -> str:
        return "\n".join([self.verse(n) for n in range(a, b - 1, -1)])

    def verse(self, n: int) -> str:
        match n:
            case 7:
                return (
                    "7 bottles of beer on the wall, "
                    "7 bottles of beer.\n"
                    "Take one down and pass it around, "
                    "1 six-pack of beer on the wall.\n"
                )
            case 6:
                return (
                    "1 six-pack of beer on the wall, "
                    "1 six-pack of beer.\n"
                    "Take one down and pass it around, "
                    "5 bottles of beer on the wall.\n"
                )
            case 2:
                return (
                    "2 bottles of beer on the wall, "
                    "2 bottles of beer.\n"
                    "Take one down and pass it around, "
                    "1 bottle of beer on the wall.\n"
                )
            case 1:
                return (
                    "1 bottle of beer on the wall, "
                    "1 bottle of beer.\n"
                    "Take it down and pass it around, "
                    "no more bottles of beer on the wall.\n"
                )
            case 0:
                return (
                    "No more bottles of beer on the wall, "
                    "no more bottles of beer.\n"
                    "Go to the store and buy some more, "
                    "99 bottles of beer on the wall.\n"
                )
            case _:
                return (
                    f"{n} bottles of beer on the wall, "
                    f"{n} bottles of beer.\n"
                    "Take one down and pass it around, "
                    f"{n - 1} bottles of beer on the wall.\n"
                )
