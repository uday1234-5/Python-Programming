import random as rand
class Dice:
    def roll_dice(self):
        print(f"After rolling dice, we get : {rand.randint(1,6)}")
d1 = Dice()
while 1:
    d1.roll_dice()