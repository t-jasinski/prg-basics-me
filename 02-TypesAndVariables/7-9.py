import random
dice_roll = random.randint(1,6)
roll_good = dice_roll == 1 or dice_roll == 6
print(f'Dice roll: {dice_roll}')
print(f'Is it a good roll? {roll_good}')