import tkinter as tk

def change_color():
    # Get the values from the entry boxes
    red = int(red_entry.get())
    green = int(green_entry.get())
    blue = int(blue_entry.get())

    # Validate the input values (between 0-255)
    if red < 0 or red > 255 or \
        green < 0 or green > 255 or \
        blue < 0 or blue > 255:
        status_label.config(text="Please enter values between 0-255")
        return

    # Format the RGB values for the color
    color = "#%02x%02x%02x" % (red, green, blue)

    # Set the color label background
    color_label.config(bg=color)
    status_label.config(text="Color changed successfully")

# Create the main window
window = tk.Tk()
window.title("Color Changer")

# Create the entry boxes
red_label = tk.Label(window, text="Red (0-255):")
red_label.pack()
red_entry = tk.Entry(window)
red_entry.pack()

green_label = tk.Label(window, text="Green (0-255):")
green_label.pack()
green_entry = tk.Entry(window)
green_entry.pack()

blue_label = tk.Label(window, text="Blue (0-255):")
blue_label.pack()
blue_entry = tk.Entry(window)
blue_entry.pack()

# Create the button to change the color
change_button = tk.Button(window, text="Change Color", command=change_color)
change_button.pack()

# Create the status label
status_label = tk.Label(window)
status_label.pack()

# Create the label to display the color
color_label = tk.Label(window, width=30, height=10)
color_label.pack()

# Run the main loop
window.mainloop()
