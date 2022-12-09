from tkinter import *
import math

base=Tk()
canvas=Canvas(base,width=800,height=1000,background='black')
canvas.pack()


center_x=400
center_y=500
r=50 # The distance from the center point to each angle, called the radius

# Place the five points of the five-pointed star in turn
points=[

center_x-int(r*math.sin(2*math.pi/5)),
center_y-int(r*math.cos(2*math.pi/5)),

#
center_x+int(r*math.sin(2*math.pi/5)),
center_y-int(r*math.cos(2*math.pi/5)),

#
center_x-int(r*math.sin(math.pi/5)),
center_y+int(r*math.cos(math.pi/5)),

# vertex
center_x,
center_y-r,

#
center_x+int(r*math.sin(math.pi/5)),
center_y+int(r*math.cos(math.pi/5)),
]
# Create a polygon based on ten vertices
canvas.create_polygon(points,outline='white',fill='white')

center_x=100
center_y=100
r=50 # The distance from the center point to each angle, called the radius

# Place the five points of the five-pointed star in turn
points=[

center_x-int(r*math.sin(2*math.pi/5)),
center_y-int(r*math.cos(2*math.pi/5)),

#
center_x+int(r*math.sin(2*math.pi/5)),
center_y-int(r*math.cos(2*math.pi/5)),

#
center_x-int(r*math.sin(math.pi/5)),
center_y+int(r*math.cos(math.pi/5)),

# vertex
center_x,
center_y-r,

#tt
center_x+int(r*math.sin(math.pi/5)),
center_y+int(r*math.cos(math.pi/5)),
]
# Create a polygon based on ten vertices
canvas.create_polygon(points,outline='white',fill='white')

canvas.create_line(100,100,400,500, width = 2,  fill='white')

base.mainloop()
