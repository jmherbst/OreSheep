#/usr/bin/env python
import random
import sys

class DiceCup:
  def __init__(self, dice):
    self.dice = dice

  def toss(self):
    rolls = []
    ore_or_sheep = ''

    for dice in self.dice:
      rolls.append(dice.roll())

    if sum(rolls) % 3 == 0 and sum(rolls) % 4 == 0:
      ore_or_sheep = ' -- [ OreSheep ]' 
    elif sum(rolls) % 3 == 0:
      ore_or_sheep = '  -- [ Ore ]'
    elif sum(rolls) % 4 == 0:
      ore_or_sheep = '  -- [ Sheep ]' 

    print('Roll: {} -- Combined: {} {}'.format(
              ', '.join([str(roll) for roll in rolls]),
              sum(rolls),
              ore_or_sheep,
            )
         )

class Dice:
  def __init__(self, sides=6):
    self.sides = sides

  def roll(self):
    return random.randint(1, self.sides)
  
cup = DiceCup([Dice(6), Dice(6)])
number_of_rolls = 11

if len(sys.argv) == 1:
  print('No number of rolls given.  Defaulting to {}.'.format(number_of_rolls))
elif len(sys.argv) > 1:
  try:
    int(sys.argv[1])
    number_of_rolls = int(sys.argv[1])
  except:
    print('No valid number of rolls provided.  Defaulting to {}.'.format(number_of_rolls))

for x in range(0, number_of_rolls):
  cup.toss() 

