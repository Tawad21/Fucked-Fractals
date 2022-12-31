import tkinter as tk
import math

def draw_star(points, length):
    # Draw a line from the first point to the last point
    x1, y1 = points[0]
    x2, y2 = points[-1]
    canvas.create_line(x1, y1, x2, y2)

    # Calculate the new point using polar coordinates
    x3, y3 = points[1]
    r = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    theta = math.atan2(y2 - y3, x2 - x3) + math.pi/3
    x4 = x3 + r * math.cos(theta)
    y4 = y3 + r * math.sin(theta)

    # Draw a line from the last point to the new point
    canvas.create_line(x2, y2, x4, y4)

def star(points, order, length, iterations):
    if order > iterations:
        # Base case: draw a single star
        draw_star(points, length)
    else:
        # Recursive case: draw five smaller stars
        for i in range(5):
            star(points, order + 1, length/3, iterations)
            points = points[1:] + points[:1]

# Create a Tkinter canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Set the initial points for the star
points = [(300, 100), (400, 200), (500, 100), (450, 300), (500, 500), (300, 400), (100, 500), (150, 300), (300, 100)]

# Prompt the user for the number of iterations
iterations = int(input("Enter the number of iterations: "))

# Plot the star fractal
star(points, 0, 300, iterations)

tk.mainloop()