from tkinter import *

def color_box():
    # Retrieve the RGB values from the Entry widgets
    red = int(red_entry.get())
    green = int(green_entry.get())
    blue = int(blue_entry.get())
    
    # Check if the values are within the valid range (0-255)
    if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
        # Convert the RGB values to a hexadecimal color code
        color_code = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
        
        # Configure the background color of the box label
        box_label.config(bg=color_code)
    else:
        # Display an error message if the RGB values are invalid
        box_label.config(text="Invalid RGB values", bg="white")

# Create the main window
window = Tk()

# Create Entry widgets for each RGB value
red_label = Label(window, text="Red:")
red_label.pack()
red_entry = Entry(window)
red_entry.pack()

green_label = Label(window, text="Green:")
green_label.pack()
green_entry = Entry(window)
green_entry.pack()

blue_label = Label(window, text="Blue:")
blue_label.pack()
blue_entry = Entry(window)
blue_entry.pack()

# Create the button to trigger the color change
color_button = Button(window, text="Color Box", command=color_box)
color_button.pack()

# Create the label representing the colored box
box_label = Label(window, width=20, height=10, bg="white")
box_label.pack()

# Start the main event loop
window.mainloop()
