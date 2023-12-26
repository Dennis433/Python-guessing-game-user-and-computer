import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess > random_number:
            print('Your guess is high')
        if guess < random_number:
            print('Your guess is low')
    print(f'Congrats you guessed the number: {random_number} correctly')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback!= 'c':
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low #could also be high
        feedback = input(f'Is the number {computer_guess} correct "C",  high "H" or low "L"?? :').lower()
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1
    print(f'yay the computer guessed your number {computer_guess} correctly')
computer_guess(100)

