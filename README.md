# Arabic Text Cleaner

This is a Python program that allows you to modify Arabic text by performing various operations such as removing diacritization, removing numbers, removing HTML tags, removing duplicates, removing extra spaces, and copying the cleaned output.

## Prerequisites
- Python 3.x
- Required Python modules: `tkinter`, `arabic_reshaper`, `bidi`, `pyperclip`, `re`

## Installation
1. Install Python 3.x on your machine. You can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

2. Install the required Python modules using pip:

## Usage
1. Run the `ArabicCleaner.py` file using Python:

2. The graphical user interface (GUI) will be displayed with a text box and several buttons.

3. Enter your Arabic text in the text box.

4. Click on the desired button to perform the corresponding text modification operation.

5. The modified text will be displayed in the text box, and you can also copy it to the clipboard by clicking the "Copy Output" button.

6. Hover over a button to see a brief description of its functionality in the info label at the bottom.

7. Close the program by closing the GUI window.

## Functionality

### Remove Diacritization
- Clicking the "Remove Diacritization" button removes all diacritization (Tashkil) from the text.

### Remove Numbers
- Clicking the "Remove Numbers" button removes all numbers from the text.

### Remove HTML Tags
- Clicking the "Remove HTML Tags" button removes all HTML tags and special characters (e.g., <>, /) from the text.

### Remove Duplicates
- Clicking the "Remove Duplicates" button removes all duplicated words and symbols from the text.

### Copy Output
- Clicking the "Copy Output" button copies the cleaned text in the correct Arabic format to the clipboard.

### Remove Extra Spaces
- Clicking the "Remove Extra Spaces" button removes all double or more spaces and replaces them with a single space.

## Additional Information
- The program uses the `tkinter` module for creating the GUI.
- The `arabic_reshaper` module is used to reshape Arabic text for proper display in the GUI.
- The `bidi` module is used to handle bidirectional text for correct Arabic rendering.
- The `pyperclip` module is used to copy text to the clipboard.
- The `re` module is used for performing regular expression operations.
- The GUI is designed using the grid layout manager to arrange the buttons and text box.

Please make sure to install the required Python modules and run the program using Python 3.x.

For any issues or inquiries, please contact [Karmouch Mehdi] at [mehdi.karmouch@edu.umi.ac.ma].
Check out my personal website: [Karmouch.me](https://karmouch.me)

Note: This program is provided as-is without any warranty. Use it at your own risk.
