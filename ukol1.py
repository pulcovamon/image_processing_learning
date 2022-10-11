# nastavení uhádnutí čísla na false
from random import randint

# set win to false
win = False

# set limits
lim_low = 0
lim_high = 20

# choose random number
number = randint(lim_low, lim_high)

# repeat until the number is guessed
while not win:
    guess = int(input(f'Guess number between {lim_low} and {lim_high}: '))

    # go back to the shadow (ehm start)
    if guess < lim_low or guess > lim_high:
        print('Your guess is outside the limit!')
        continue

    # stop the game if the guess is right
    if guess == number:
        win = True
        print('well done!')

    # set limits of the guess
    elif guess > number:
        print('Number is smaller than your guees.\nTry it again!')
        lim_high = guess - 1
    else:
        print('Number is greater than your guees.\nTry it again!')
        lim_low = guess + 1