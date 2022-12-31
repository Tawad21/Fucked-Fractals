import tkinter as tk
import math

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

# Define a function to convert polar coordinates to Cartesian coordinates
def polar_to_cartesian(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

# Define a recursive function to draw the star
def draw_star(size, x, y, theta):
    # Base case: if the size is too small, stop recursing
    if size < 5:
        return

    # Calculate the points of the star in polar coordinates
    p1 = (size, theta)
    p2 = (size / 3, theta - math.pi / 6)
    p3 = (size, theta - math.pi / 3)
    p4 = (size - size / 3, theta - math.pi / 2)
    p5 = (size, theta - 2 * math.pi / 3)
    p6 = (size / 3, theta - 5 * math.pi / 6)
    p7 = (size, theta - math.pi)
    p8 = (size / 3, theta - 7 * math.pi / 6)
    p9 = (size, theta - 4 * math.pi / 3)
    p10 = (size - size / 3, theta - 3 * math.pi / 2)
    p11 = (size, theta - 5 * math.pi / 3)
    p12 = (size / 3, theta - 11 * math.pi / 6)

    # Convert the polar coordinates to Cartesian coordinates
    points = []
    for r, t in (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        x_point, y_point = polar_to_cartesian(r, t)
        points.append(x + x_point)
        points.append(y - y_point)

    # Draw the star using the calculated points
    canvas.create_polygon(*points, fill="white", outline="black")

    # Recursively draw smaller stars
    draw_star(size / 3, x, y - size / 3, theta - math.pi / 3)
    draw_star(size / 3, x + size - size / 3, y, theta - math.pi / 2)
    draw_star(size / 3, x, y + size / 3, theta - 2 * math.pi / 3)
    draw_star(size / 3, x - size + size / 3, y, theta - math.pi)

# Initial call to draw the star
draw_star(size, x, y, 0)

# Run the Tkinter event loop
window.mainloop()