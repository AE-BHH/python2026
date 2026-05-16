import random

coin = random.choice(["heads", "tails"])
# print(coin)

number = random.randint(1, 5)
print(number)

cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)
