import random as r

num = r.randrange(100)
guess = 5

while guess >=0:
    your_guess =int(input('Enter your guess: '))

    def check(x):
        if your_guess == x:
            print('You Win')
        elif your_guess > x :
            print('guess again whith less value')
        else:
            print('guess a higher num')

    if guess> 1:
        check(num)
    elif guess == 1:
        check(num)
        print('this is your last chance ')
    else:
        print('you lost')
    guess -= 1
