class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    return '\n'.join(self.verse(i) for i in range(upper, lower-1, -1))

  def verse(self, number):
    bottle_number = self.bottle_number_given(number)
    next_bottle_number = self.bottle_number_given(bottle_number.successor())

    return (
      f'{bottle_number} of beer on the wall, '.capitalize() +
      f'{bottle_number} of beer.\n'
      f'{bottle_number.action()}, '
      f'{next_bottle_number} of beer on the wall.\n'
    )

  @staticmethod
  def bottle_number_given(number):
    return BottleNumber(number)

class BottleNumber:
  def __init__(self, number):
    self.number = number

  def __str__(self):
    return f'{self.quantity()} {self.container()}'

  def quantity(self):
    if self.number == 0:
      return 'no more'
    return str(self.number)

  def container(self):
    if self.number == 1:
      return 'bottle'
    return 'bottles'

  def action(self):
    if self.number == 0:
        return 'Go to the store and buy some more'
    return f'Take {self.pronoun()} down and pass it around'

  def pronoun(self):
    if self.number == 1:
      return 'it'
    return 'one'

  def successor(self):
    if self.number == 0:
      return 99
    return self.number - 1

class BottleNumber0(BottleNumber):
  def quantity(self):
    return 'no more'
