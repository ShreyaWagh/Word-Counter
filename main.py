import tkinter as tk
from tkinter import ttk
from collections import Counter

def count_words():
    # Get the text from the entry widget
    text = entry.get()
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Count the number of words
    num_words = len(words)
    # Update the label with the word count
    word_count_label.config(text="Number of words: " + str(num_words))
    # Count word frequency
    word_freq = Counter(words)
    # Update the word frequency label
    word_freq_label.config(text="Word Frequency: " + str(word_freq))

def clear_text():
    # Clear the text entry field
    entry.delete(0, tk.END)
    # Clear the labels
    word_count_label.config(text="")
    word_freq_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Word Count")

# Set the background color
root.configure(background="#C6ECCF")

# Set the style for the widgets
style = ttk.Style()
style.configure("TButton", padding=5, font=("Helvetica", 10), background="#C6ECCF")  # Blue
style.configure("TEntry", padding=5, font=("Helvetica", 10), background="#C6ECCF")
style.configure("TLabel", padding=5, font=("Helvetica", 10), background="#C6ECCF")  # Light gray

# Create an entry widget for the user to enter text
entry = ttk.Entry(root, width=50)
entry.pack(pady=10)

# Create a frame to hold the buttons and center it
button_frame = ttk.Frame(root)
button_frame.pack()



# Create a button to trigger the word count function
count_button = ttk.Button(button_frame, text="Count Words", command=count_words ,)
count_button.pack(side=tk.LEFT, padx=5, pady=10)

# Create a button to clear the text entry field
clear_button = ttk.Button(button_frame, text="Clear Text", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5, pady=10)

# Create a label to display the word count
word_count_label = ttk.Label(root, text="")
word_count_label.pack(pady=5)

# Create a label to display the word frequency
word_freq_label = ttk.Label(root, text="")
word_freq_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()