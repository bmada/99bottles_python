import unittest
from bottles import Bottles


class BottlesTest(unittest.TestCase):
  def test_the_first_verse(self):
    expected = (
      '99 bottles of beer on the wall, '
      '99 bottles of beer.\n'
      'Take one down and pass it around, '
      '98 bottles of beer on the wall.\n'
    )
    self.assertEqual(Bottles().verse(99), expected)
