import tkinter as tk
import math

def simple_star(x, y, r):
    
    a = [x-int(r*math.sin(2*math.pi/5)), y-int(r*math.cos(2*math.pi/5))]
    b = [x+int(r*math.sin(2*math.pi/5)), y-int(r*math.cos(2*math.pi/5))]
    c = [x-int(r*math.sin(math.pi/5)), y+int(r*math.cos(math.pi/5))]
    d = [x, y-r]
    e = [x+int(r*math.sin(math.pi/5)), y+int(r*math.cos(math.pi/5))]
    
    points = [a, b, c, d, e, a]

    canvas.create_line(points)  
    

def star_fractal(x, y, r):
    if r < 1: 
        return
    simple_star(x, y, r)
    star_fractal(x, y, r-100)

    


root = tk.Tk()
root.title('Cancer Constellation Fractals')

canvas = tk.Canvas(root, width=800, height=1000, bg='white')
canvas.pack()


star_fractal(400, 500, 400)



root.mainloop()
    
