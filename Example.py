import tkinter as tk
from tkinter import messagebox

# Set of bad words
bad_words = {"bad", "words", "school","coding"}

# Function to check if a message contains bad words
def check_message(message):
    words = message.split()
    for word in words:
        if word.lower() in bad_words:
            return False
    return True

# Function to add a message to the conversation
def send_message():
    message = message_box.get("1.0", "end-1c")
    if check_message(message):
        conversation.insert("end", message + "\n")
        message_box.delete("1.0", "end")
    else:
        messagebox.showerror("Error", "Sorry, your message did not deliver because it contains inappropriate words.")
        message_box.delete("1.0", "end")

# Create the main window
window = tk.Tk()
window.title("Messaging System")

# Create the conversation area
conversation = tk.Text(window)
conversation.pack()

# Create the message box
message_box = tk.Text(window)
message_box.pack()

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Start the main loop
window.mainloop()
