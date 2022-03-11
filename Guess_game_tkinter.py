from tkinter import Tk, Button, Label, Entry, END
from random import randint

from Guess_game import explanation, check_guess, return_winfeedback


root = Tk()



class number():
    '''An omit for using global'''
    def __init__(self):
        self.count = 0

    def increase_times_guessed(self):
        self.count += 1


def take_guess(guess):
    '''Takes and controlls the guess, and then giving feedback on that guess'''
    guess_in.delete(0, END)
    try:
        guess = int(guess)
    except ValueError:
        Label(root, text='That is not a number, put in a number!').pack()
    else:
        times_guessed.increase_times_guessed()
        check = check_guess(guess, random_number)
        if check[0] == True:
            Label(root, text=return_winfeedback(times_guessed.count)).pack()
            root.quit()
        else:
            feedback = f'{guess} is too {check[0]}, guess something {check[1]}.'
            Label(root, text = feedback).pack()


def tab_pressed(event):
    '''An omit for using lambda, becouse that was causing an error. '''
    take_guess(guess_in.get())

    
# Giving some defenitions I will need later
goguess = 'Guess a number:'
button_text = 'Guess'
random_number = randint(1, 100)
times_guessed = number()

# Defining all these variables so I can Use and Pack() them later
explanation = Label(root, text=explanation)
goguess = Label(root, text=goguess)
guess_in = Entry(root)
button = Button(root, text=button_text, command=lambda: take_guess(guess_in.get()))
button.bind('<FocusIn>', tab_pressed)

# Packing these defenitions
explanation.pack()
goguess.pack()
guess_in.pack()
button.pack()

root.mainloop()
