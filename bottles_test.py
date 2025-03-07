import pytest

from bottles import CountdownSong
from bottles import BottleVerse
from bottles import BottleNumber
from bottles import BottleNumber0
from bottles import BottleNumber1
from bottles import BottleNumber6


def responds_to_lyrics(role_player):
    return hasattr(role_player, 'lyrics') and callable(role_player.lyrics)


class VerseFake:
    @staticmethod
    def lyrics(number):
        return f'this is verse {number}.\n'


class TestVerseFake:
    def test_plays_verse_role(self):
        assert responds_to_lyrics(VerseFake)


class TestCountdownSong:
    def test_verse(self):
        expected = 'this is verse 500.\n'
        assert CountdownSong(verse_template=VerseFake).verse(500) == expected

    def test_verses(self):
        expected = (
            'this is verse 99.\n'
            '\n'
            'this is verse 98.\n'
            '\n'
            'this is verse 97.\n'
        )
        assert CountdownSong(verse_template=VerseFake).verses(99, 97) == expected

    def test_song(self):
        expected = (
            'this is verse 50.\n'
            '\n'
            'this is verse 49.\n'
            '\n'
            'this is verse 48.\n'
        )
        assert CountdownSong(
            verse_template=VerseFake,
            max=50,
            min=48,
        ).song() == expected


class TestBottleVerse:
    def test_plays_verse_role(self):
        assert responds_to_lyrics(BottleVerse)

    def test_verse_general_rule_upper_bound(self):
        expected = (
            '99 bottles of beer on the wall, '
            '99 bottles of beer.\n'
            'Take one down and pass it around, '
            '98 bottles of beer on the wall.\n'
            )
        assert BottleVerse.lyrics(99) == expected

    def test_verse_general_rule_lower_bound(self):
        expected = (
            '3 bottles of beer on the wall, '
            '3 bottles of beer.\n'
            'Take one down and pass it around, '
            '2 bottles of beer on the wall.\n'
            )
        assert BottleVerse.lyrics(3) == expected


    def test_verse_7(self):
        expected = (
            '7 bottles of beer on the wall, '
            '7 bottles of beer.\n'
            'Take one down and pass it around, '
            '1 six-pack of beer on the wall.\n'
            )
        assert BottleVerse.lyrics(7) == expected


    def test_verse_6(self):
        expected = (
            '1 six-pack of beer on the wall, '
            '1 six-pack of beer.\n'
            'Take one down and pass it around, '
            '5 bottles of beer on the wall.\n'
            )
        assert BottleVerse.lyrics(6) == expected


    def test_verse_2(self):
        expected = (
            '2 bottles of beer on the wall, '
            '2 bottles of beer.\n'
            'Take one down and pass it around, '
            '1 bottle of beer on the wall.\n'
            )
        assert BottleVerse.lyrics(2) == expected


    def test_verse_1(self):
        expected = (
            '1 bottle of beer on the wall, '
            '1 bottle of beer.\n'
            'Take it down and pass it around, '
            'no more bottles of beer on the wall.\n'
            )
        assert BottleVerse.lyrics(1) == expected


    def test_verse_0(self):
        expected = (
            'No more bottles of beer on the wall, '
            'no more bottles of beer.\n'
            'Go to the store and buy some more, '
            '99 bottles of beer on the wall.\n'
            )
        assert BottleVerse.lyrics(0) == expected



def test_returns_correct_class_for_given_number():
    # 0, 1, 6 are special
    assert BottleNumber(0).__class__ == BottleNumber0
    assert BottleNumber(1).__class__ == BottleNumber1
    assert BottleNumber(6).__class__ == BottleNumber6

    # others are not special
    assert BottleNumber(9).__class__ == BottleNumber
    assert BottleNumber(35).__class__ == BottleNumber

