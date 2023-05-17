import random
import pyautogui

def guess():
    attempts = 0
    while True:
        guess = int(pyautogui.prompt("Guess the number (between 1 and 100):"))
        attempts += 1
        
        if guess < number:
            pyautogui.alert("Too low! Try again.")
        elif guess > number:
            pyautogui.alert("Too high! Try again.")
        else:
            pyautogui.alert(f"You guessed the number {number} correctly in {attempts} attempts!")
            break

def reset_game():
    global target_number
    number = random.randint(1, 100)

# Generate random target number
number = random.randint(1, 100)

# Open the game window by launching the input dialog using PyAutoGUI
pyautogui.alert("Welcome to the Greatest Number Guessing Game!")

# Use PyAutoGUI's automation capabilities to interact with the GUI
guess()
