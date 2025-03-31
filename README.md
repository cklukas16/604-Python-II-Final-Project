# Course work for St. Thomas Software Engineering Program
## SEIS 604 - Python II

## Mastermind Game
A Python script implements the rules of a classic logic game. 
Tkinter GUI tools are used to create a simple user interface. 

### Ongoing work
Improve design by incorporating Object Oriented concepts.
 - GameBoard class: builds the GUI elements; displays the guess; displays the clues/result
 - Code class: generates and holds the secret code; checks guess against secret code
 - Play/Turn class: holds the guess
 - Game class: main driver; creates the board; holds the total number of guesses; provides feedback on guess accuracy

### Notes:
 - Original colour module was not compatible with updated Python & Tkinter versions. Modified 2025.
 - MacOS integrated Python version has many known bugs related to Tkinter. Manual install with virtual environment using Python 3.13 was required.
 - MacOS is currently unable to display button colors using Tkinter. Known issue. 
