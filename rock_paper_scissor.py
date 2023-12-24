import tkinter as tk
import random

def play_game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user_choice, computer_choice, result):
    result_text.set(f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry('400x300+600+200')
root.resizable(False, False)

# Variables
choices = ["Rock", "Paper", "Scissors"]
result_text = tk.StringVar()


# Widgets
label = tk.Label(root, text="Choose your move:",font=('bold',10))
label.pack(pady=20)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

for choice in choices:
    button = tk.Button(buttons_frame, text=choice, command=lambda c=choice: play_game(c))
    button.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 12, "bold"))
result_label.pack(pady=30)

# Run the main loop
root.mainloop()
