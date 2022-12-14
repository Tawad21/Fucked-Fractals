import tkinter as tk 
import math 
root=tk.Tk()
root.title("Cancer constellation Fractals")

canvas=tk.Canvas(root, width=900,height=900,bg="black")
canvas.pack()
def rotate(origin,point,angle):
     ox,oy=origin 
     px,py=point 
     qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
     qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
     return [qx,qy]

def simple_star(x,y,r,color1,color2):
     a = [x-int(r*math.sin(2*math.pi/5)), y-int(r*math.cos(2*math.pi/5))]
     b = [x+int(r*math.sin(2*math.pi/5)), y-int(r*math.cos(2*math.pi/5))]
     c = [x-int(r*math.sin(math.pi/5)), y+int(r*math.cos(math.pi/5))]
     d = [x, y-r]
     e = [x+int(r*math.sin(math.pi/5)), y+int(r*math.cos(math.pi/5))]
     points = [a, b, c, d, e, a]
     canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline='cyan2', fill='black')
     canvas.create_polygon(points, width=2, outline='green2', fill=color1)
     new_points = []
     for i in points:
             new_point = rotate([x, y], i, math.pi/5)
             new_points.append(new_point)
     canvas.create_polygon(new_points, width=2, outline='yellow', fill=color2)  

def star_fractals(x,y,r,color1,color2):
     if r<1:
             return 
     simple_star(x,y,r,color1,color2)
     star_fractals(x,y,r*1/2.62,color2,color1)
 
star_fractals(450,450,400,"blue4","orangeRed2")
root.mainloop()
