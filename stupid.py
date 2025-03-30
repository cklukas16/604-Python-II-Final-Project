
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from enum import Enum
import random

class COLORS(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"
    YELLOW = "Yellow"
    PINK = "Pink"
    ORANGE = "Orange"

print(tk.TkVersion)

##__________________________________________________________________________________________________________________##
## Code class ##
# Uses COLORS Enum to create a list of colors used to generate the secret code.
class Code():
    def __init__(self):
        self.colors = []
        for i in COLORS:
            self.colors.append(i.value)

    # Returns a list of 4 colors in random order.
    def secret_code(self):
        return random.sample(self.colors, 4)

    # Validation. Checks that guess is only 4 items in length. Used by play() in Game class.
    # Displays an error message box.
    def code_check(self, guess):
        if len(guess) != 4:
            messagebox.showwarning("Invalid Input", "Guess must contain exactly 4 colors.")
            return False
        return True

##__________________________________________________________________________________________________________________##
## Create the Tkinter GUI ##
root = tk.Tk()
root.title("Mastermind Game")
root.config(bg="skyblue")

## Create GUI frames ##
# Upper frame holds instructions
upper_frame = Frame(root, width=1000, height=100, bg='skyblue')
upper_frame.grid(row=0, columnspan=3, padx=5, pady=5)

# Upper frame2 contains label for user guess text.
upper_frame2 = Frame(root, width=1000, height=100, bg='skyblue')
upper_frame2.grid(row=1, columnspan=3, padx=5, pady=5)

# Left frame holds buttons for guessing, new game, etc.
left_frame = Frame(root, width=300, height=400, bg='skyblue')
left_frame.grid(row=2, column=0, padx=5, pady=5)

# Center frame holds a record of guesses.
center_frame = Frame(root, width=300, height=400, bg='skyblue')
center_frame.grid(row=2, column=1, padx=5, pady=5)

# Right frame holds a record of clues/hints
right_frame = Frame(root, width=300, height=400, bg='skyblue')
right_frame.grid(row=2, column=2, padx=5, pady=5)

# Frame Lists: Used by clear display() for new game & clear guess buttons.
display_frames = [center_frame, right_frame]
guess_text = [upper_frame2]

##__________________________________________________________________________________________________________________##
## Create GUI labels and buttons ##
entry_label = tk.Label(upper_frame, text="Guess the secret code by entering a 4-color guess using the buttons below. "
                                         "The secret code contains 4 different colors. \n"
                                         "Use the clues to refine your guess: \n "
                                         "Grey Peg = One color is not in the secret code. \n"
                                         "White Peg = One correct color in the wrong location. \n"
                                         "Black Peg = One correct color in the right location.")
entry_label.grid(row=0, column=0, padx=10, pady=10)

