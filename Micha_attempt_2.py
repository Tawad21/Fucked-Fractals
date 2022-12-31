import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()

# Set the window title
window.title("Fractal Star")

# Create a canvas to draw on
canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

# Set the initial size and position of the star
size = 200
x = 300
y = 300

# Define a recursive function to draw the star
def draw_star(size, x, y):
    # Base case: if the size is too small, stop recursing
    if size < 5:
        return

    # Calculate the points of the star
    p1 = (x, y - size)
    p2 = (x + size / 3, y - size / 3)
    p3 = (x + size, y - size / 3)
    p4 = (x + size - size / 3, y)
    p5 = (x + size, y + size / 3)
    p6 = (x + size / 3, y + size / 3)
    p7 = (x, y + size)
    p8 = (x - size / 3, y + size / 3)
    p9 = (x - size, y + size / 3)
    p10 = (x - size + size / 3, y)
    p11 = (x - size, y - size / 3)
    p12 = (x - size / 3, y - size / 3)

    # Draw the star using the calculated points
    canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, fill="white", outline="black")

    # Recursively draw smaller stars
    draw_star(size / 3, x, y - size / 3)
    draw_star(size / 3, x + size - size / 3, y)
    draw_star(size / 3, x, y + size / 3)
    draw_star(size / 3, x - size + size / 3, y)

# Initial call to draw the star
draw_star(size, x, y)

# Run the Tkinter event loop
window.mainloop()