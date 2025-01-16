# import random
#
# coin = random.choice(["heads", "tails"]) #takes in a list and gives out value randomly
# print(coin)
import random

from random import choice   ### just use choice not all the other .random options

from wheel.macosx_libfile import calculate_macosx_platform_tag

coin = choice(["heads", "tails"])
print(f"{coin}")


from random import randint

number = randint(1, 10)
print(number)


from random import shuffle

cards = ["jack", "queen", "king", "ace"]
shuffle(cards)
for item in cards:
    print(item)

