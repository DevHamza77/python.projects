import random

cards = [ "jack", "queen", "king", "ace" ]
random.shuffle(cards)
for card in cards:
    print(card)

# A library called random has been imported that allows us access to all its functions
# A list of cards has been given and stored in the variable 'cards'
# The function 'shuffle' from 'random' library has been used that shuffles every string/value
# for loop has been used that iterates and prints one card at a time after shuffling it 
