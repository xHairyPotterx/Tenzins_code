from random import randint
from time import sleep

explanation = '''
Welcome to guessing the number! Here is how it works:
Guess a number between 0 and 100. Then it tells you if you need to guess higher or lower.
Then guess a number higher or lower depending on your previous answer. 
Continue until you guessed the number.
'''.lstrip()
number_list = []

def check_guess(guess, the_number):
    if guess > the_number:
        return ['High', 'Lower']
    elif guess < the_number:
        return ['Low', 'Higher']
    elif guess == the_number:
        return [True]


def return_winfeedback(times_guessed):
    if times_guessed == 1:
        return 'You guessed the number first try!'
    else:
        return f'You guessed the number! It took you {times_guessed} guesses.'


def start_guessing():
    print(explanation)
    count = 0
    random_number = randint(1, 100)
    while True:
        try:
            guess = int(input('Guess a number: '))
        except ValueError:
            print('Thats not a number! Put in a number!')
            continue
        if guess in number_list:
            print('You already guessed that number!')
            continue
        number_list.append(guess)
        count += 1
        check = check_guess(guess, random_number)
        if check[0] == True:
            print(return_winfeedback(count))
            sleep(3)
            break
        else:
            print(f'This number is too {check[0]}. Guess something {check[1]}.')

start_guessing()
