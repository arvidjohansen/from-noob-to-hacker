import tkinter as tk
import winsound
import time

# Morse Code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}

REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

# Function to beep with a duration (dot or dash)
def beep(duration):
    winsound.Beep(1000, duration)  # 1000 Hz frequency
    time.sleep(0.1)  # Short pause between beeps

# Function to handle dot button
def add_dot():
    morse_input.insert(tk.END, ".")
    beep(200)
    guess_message()

# Function to handle dash button
def add_dash():
    morse_input.insert(tk.END, "-")
    beep(600)
    guess_message()

# Function to clear the input field
def clear_input():
    morse_input.delete(1.0, tk.END)
    guessed_output.config(text="")

# Function to guess the letter from morse input
def guess_message():
    code = morse_input.get(1.0, tk.END).strip()
    guessed_letter = REVERSE_MORSE_CODE_DICT.get(code, "Invalid Morse")
    guessed_output.config(text=f"Guessed Letter: {guessed_letter}")

# Creating the main window
root = tk.Tk()
root.title("Morse Code Practice")
root.geometry("500x400")

# Creating UI elements
title_label = tk.Label(root, text="Morse Code Practice", font=("Arial", 16))
title_label.pack(pady=10)

# Display Morse Code reference
morse_ref_frame = tk.Frame(root)
morse_ref_frame.pack(pady=5)

morse_ref_label = tk.Label(morse_ref_frame, text="Morse Alphabet", font=("Arial", 12))
morse_ref_label.grid(row=0, column=0, columnspan=2)

morse_table = tk.Text(morse_ref_frame, height=10, width=30)
morse_table.grid(row=1, column=0, columnspan=2)

# Filling the Morse alphabet into the text box (for reference)
for letter, code in MORSE_CODE_DICT.items():
    morse_table.insert(tk.END, f"{letter}: {code}\n")
morse_table.config(state=tk.DISABLED)

# Input area for Morse code
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

morse_input_label = tk.Label(input_frame, text="Enter Morse Code (. and -):")
morse_input_label.grid(row=0, column=0, columnspan=2)

morse_input = tk.Text(input_frame, height=1, width=30)
morse_input.grid(row=1, column=0, columnspan=2)

# Buttons for adding dot, dash, and clearing input
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

dot_button = tk.Button(button_frame, text="Dot (.)", command=add_dot, width=10)
dot_button.grid(row=0, column=0, padx=5)

dash_button = tk.Button(button_frame, text="Dash (-)", command=add_dash, width=10)
dash_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_input, width=10)
clear_button.grid(row=0, column=2, padx=5)

# Label to display guessed output
guessed_output = tk.Label(root, text="", font=("Arial", 14))
guessed_output.pack(pady=10)

# Run the main event loop
root.mainloop()
