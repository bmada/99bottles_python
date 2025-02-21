from __future__ import annotations

class BottleNumber:
    _registry = []

    def __init__(self, number: int):
        self._number = number

    def __str__(self):
        return f'{self.quantity()} {self.container()}'

    def __new__(cls, number: int):
        for candidate in cls._registry:
            if candidate.handles(number):
                return super().__new__(candidate)

    @classmethod
    def register(cls, candidate):
        cls._registry.insert(0, candidate)

    @staticmethod
    def handles(number: int) -> bool:
        return True

    def quantity(self) -> str:
        return f'{self._number}'

    def container(self) -> str:
        return 'bottles'

    def pronoun(self) -> str:
        return 'one'

    def action(self) -> str:
        return f'Take {self.pronoun()} down and pass it around'

    def successor(self) -> int:
        return BottleNumber(self._number - 1)

BottleNumber.register(BottleNumber)


class BottleNumber0(BottleNumber):
    def handles(number: int) -> bool:
        return number == 0

    def quantity(self) -> str:
        return 'no more'

    def action(self) -> str:
        return 'Go to the store and buy some more'

    def successor(self) -> int:
        return BottleNumber(99)

BottleNumber.register(BottleNumber0)


class BottleNumber1(BottleNumber):
    def handles(number: int) -> bool:
        return number == 1

    def container(self) -> str:
        return 'bottle'

    def pronoun(self) -> str:
        return 'it'

BottleNumber.register(BottleNumber1)


class BottleNumber6(BottleNumber):
    def handles(number: int) -> bool:
        return number == 6

    def container(self) -> str:
        return 'six-pack'

    def quantity(self) -> str:
        return '1'

BottleNumber.register(BottleNumber6)


class BottleVerse:
    def __init__(self, bottle_number: BottleNumber):
        self._bottle_number = bottle_number

    @classmethod
    def lyrics(cls, number: int):
        return cls.given(number)._lyrics()

    @classmethod
    def given(cls, number: int):
        return cls(BottleNumber(number))

    def _lyrics(self):
        return (
            f'{self._bottle_number} of beer on the wall, '.capitalize() +
            f'{self._bottle_number} of beer.\n'
            f'{self._bottle_number.action()}, '
            f'{self._bottle_number.successor()} of beer on the wall.\n'
        )


class Bottles:
    def __init__(self, verse_template=BottleVerse):
        self._verse_template = verse_template

    def verse(self, number: int) -> str:
        return self._verse_template.lyrics(number)

    def verses(self, upper: int, lower: int) -> str:
        return '\n'.join(
            self.verse(n) for n in range(upper, lower - 1, -1)
        )

    def song(self) -> str:
        return self.verses(99, 0)


class CountdownSong:
    def __init__(
        self,
        verse_template,
        max: int = 9999,
        min: int = 0,
    ):
        self._verse_template = verse_template
        self._max = max
        self._min = min

    def verse(self, number: int) -> str:
        return self._verse_template.lyrics(number)

    def verses(self, upper: int, lower: int) -> str:
        return '\n'.join(
            self.verse(n) for n in range(
                upper,
                lower - 1,
                -1,
            )
        )

    def song(self) -> str:
        return self.verses(self._max, self._min)
