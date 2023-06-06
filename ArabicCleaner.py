import tkinter as tk
from tkinter import messagebox
import arabic_reshaper
from bidi.algorithm import get_display
import pyperclip
import re

def remove_diacritization():
    input_text = input_textbox.get("1.0", "end-1c")
    reshaped_text = arabic_reshaper.reshape(input_text)
    bidi_text = get_display(reshaped_text)
    output_text = ''.join(c for c in bidi_text if not '\u064b' <= c <= '\u065f')
    input_textbox.delete("1.0", "end")
    input_textbox.insert("1.0", output_text)
    pyperclip.copy(output_text)

def remove_numbers():
    input_text = input_textbox.get("1.0", "end-1c")
    output_text = re.sub(r'\d+', '', input_text)
    input_textbox.delete("1.0", "end")
    input_textbox.insert("1.0", output_text)
    pyperclip.copy(output_text)

def remove_html_tags():
    input_text = input_textbox.get("1.0", "end-1c")
    output_text = re.sub(r'<[^>]+>', '', input_text)
    output_text = re.sub(r'[^\w\s]', '', output_text)
    input_textbox.delete("1.0", "end")
    input_textbox.insert("1.0", output_text)
    pyperclip.copy(output_text)

def remove_duplicates():
    input_text = input_textbox.get("1.0", "end-1c")
    lines = input_text.split("\n")
    cleaned_lines = []
    for line in lines:
        words = line.split()
        word_counts = {}
        cleaned_words = []
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
        for word in words:
            if word_counts[word] == 1:
                cleaned_words.append(word)
        cleaned_lines.append(" ".join(cleaned_words))
    output_text = "\n".join(cleaned_lines)
    input_textbox.delete("1.0", "end")
    input_textbox.insert("1.0", output_text)
    pyperclip.copy(output_text)


def copy_output_text():
    output_text = input_textbox.get("1.0", "end-1c")
    reshaped_text = arabic_reshaper.reshape(output_text)
    bidi_text = get_display(reshaped_text)
    pyperclip.copy(bidi_text)

def enable_editing(event):
    input_textbox.config(state=tk.NORMAL)

def display_info(message):
    info_label.config(text=message)

def remove_extra_spaces():
    input_text = input_textbox.get("1.0", "end-1c")
    cleaned_text = " ".join(input_text.split())
    input_textbox.delete("1.0", "end")
    input_textbox.insert("1.0", cleaned_text)
    pyperclip.copy(cleaned_text)

# Create the main window
window = tk.Tk()
window.title("Arabic Text Modification")
window.geometry("700x350")
window.resizable(False, False)

# Create the input text box
input_textbox = tk.Text(window, height=10, width=70, font=("Calibri", 12), wrap="word", padx=10, pady=10)
input_textbox.pack()
input_textbox.config(state=tk.DISABLED)
input_textbox.bind("<Button-1>", enable_editing)

# Create the info label in the footer
info_label = tk.Label(window, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
info_label.pack(side=tk.BOTTOM, fill=tk.X)

# Create a frame for the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Create the remove diacritization button
remove_diacritization_button = tk.Button(button_frame, text="Remove Diacritization", command=remove_diacritization)
remove_diacritization_button.grid(row=0, column=0, padx=5, pady=5)
remove_diacritization_button.bind("<Enter>", lambda event: display_info("Removes all diacritization (Tashkil) from the text"))
remove_diacritization_button.bind("<Leave>", lambda event: display_info(""))

# Create the remove numbers button
remove_numbers_button = tk.Button(button_frame, text="Remove Numbers", command=remove_numbers)
remove_numbers_button.grid(row=0, column=1, padx=5, pady=5)
remove_numbers_button.bind("<Enter>", lambda event: display_info("Removes numbers from the text"))
remove_numbers_button.bind("<Leave>", lambda event: display_info(""))

# Create the remove HTML tags button
remove_html_tags_button = tk.Button(button_frame, text="Remove HTML Tags", command=remove_html_tags)
remove_html_tags_button.grid(row=0, column=2, padx=5, pady=5)
remove_html_tags_button.bind("<Enter>", lambda event: display_info("Removes all tags and special characters ex:/<>"))
remove_html_tags_button.bind("<Leave>", lambda event: display_info(""))

# Create the remove duplicates button
remove_duplicates_button = tk.Button(button_frame, text="Remove Duplicates", command=remove_duplicates)
remove_duplicates_button.grid(row=1, column=0, padx=5, pady=5)
remove_duplicates_button.bind("<Enter>", lambda event: display_info("Removes all duplicated words and symbols"))
remove_duplicates_button.bind("<Leave>", lambda event: display_info(""))

# Create the copy output button
copy_button = tk.Button(button_frame, text="Copy Output", command=copy_output_text)
copy_button.grid(row=1, column=1, padx=5, pady=5)
copy_button.bind("<Enter>", lambda event: display_info("Copies the cleaned text in the correct format"))
copy_button.bind("<Leave>", lambda event: display_info(""))

# Create the remove extra spaces button
remove_spaces_button = tk.Button(button_frame, text="Remove Extra Spaces", command=remove_extra_spaces)
remove_spaces_button.grid(row=1, column=2, padx=5, pady=5)
remove_spaces_button.bind("<Enter>", lambda event: display_info("Removes all double and more spaces"))
remove_spaces_button.bind("<Leave>", lambda event: display_info(""))



# Start the GUI event loop
window.mainloop()
