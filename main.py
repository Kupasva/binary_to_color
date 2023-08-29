import tkinter as tk

def change_color():
    color = color_entry.get()
    window.configure(bg=color)

window = tk.Tk()
window.title("Change Window Color")

# Create a label and entry field for the color input
color_label = tk.Label(window, text="Enter color:")
color_label.pack()
color_entry = tk.Entry(window)
color_entry.pack()

# Create a button to change the color
change_button = tk.Button(window, text="Change Color", command=change_color)
change_button.pack()

window.mainloop()
