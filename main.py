import tkinter as tk

def create_box_color():
    # Get input values from the user
    r = int(entry_r.get())
    g = int(entry_g.get())
    b = int(entry_b.get())

    # Create a hexadecimal color code using the input values
    color_code = '#%02x%02x%02x' % (r, g, b)

    # Create a box with the specified color
    color_box.config(bg=color_code)

# Create a tkinter window
window = tk.Tk()
window.title("Box Color")

# Create labels and entry fields for the user to input RGB values
label_r = tk.Label(window, text="Red (0-255):")
label_r.pack()
entry_r = tk.Entry(window)
entry_r.pack()

label_g = tk.Label(window, text="Green (0-255):")
label_g.pack()
entry_g = tk.Entry(window)
entry_g.pack()

label_b = tk.Label(window, text="Blue (0-255):")
label_b.pack()
entry_b = tk.Entry(window)
entry_b.pack()

# Create a button to generate the colored box
button = tk.Button(window, text="Create Box", command=create_box_color)
button.pack()

# Create a box to display the color
color_box = tk.Label(window, width=20, height=10, relief="solid")
color_box.pack()

# Run the tkinter window
window.mainloop()
