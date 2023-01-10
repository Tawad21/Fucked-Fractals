import tkinter as tk
import math
from tkinter import colorchooser

class Main:
    def __init__(self):
        root = tk.Tk()
        root.title('Star Fractals')

        self.r = 400 # added variable to keep track of the current radius

        # Add a label, an entry, and a button to frame1
        frame1 = tk.Frame(root) # Create and add a frame to window
        frame1.pack()

        tk.Label(frame1, 
            text = "Enter the depth of star: ").pack(side = tk.LEFT)
        self.depth = tk.StringVar()
        
        tk.Entry(frame1, textvariable = self.depth, 
            justify = tk.RIGHT).pack(side = tk.LEFT)
        
        tk.Label(frame1, text = "Enter the color of star: ", padx=10,pady=10).pack(side = tk.LEFT)
        self.color = tk.StringVar()
        
        tk.Entry(frame1, textvariable=self.color).pack(side=tk.LEFT)
        
        tk.Button(frame1, text = "Display Recursive Star", 
            command = self.display).pack(side = tk.LEFT)
                
        zoom_in_button = tk.Button(frame1, text="Zoom in", command=self.zoomin, padx=10,pady=10)
        zoom_in_button.pack(side=tk.RIGHT)
        zoom_out_button = tk.Button(frame1, text="Zoom out", command=self.zoomout, padx=10,pady=10)
        zoom_out_button.pack(side=tk.RIGHT)


        # create zoom in and zoom out button

        
        self.canvas = tk.Canvas(root, width=900, height=900, bg='black')
        self.canvas.pack()

        root.mainloop() # Create an event loop

  
        
    def rotate(self, origin, point, angle):
        ox, oy = origin
        px, py = point
    
        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        
        return [qx, qy]
    
    
    def simple_star(self, x, y, r, color1, color2):
        a = [x-int(r*math.sin(2*math.pi/5)), y-int(r*math.cos(2*math.pi/5))]
        b = [x+int(r*math.sin(2*math.pi/5)), y-int(r*math.cos(2*math.pi/5))]
        c = [x-int(r*math.sin(math.pi/5)), y+int(r*math.cos(math.pi/5))]
        d = [x, y-r]
        e = [x+int(r*math.sin(math.pi/5)), y+int(r*math.cos(math.pi/5))]
        points = [a, b, c, d, e, a]
        
        self.canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline='cyan2', fill='black')
        self.canvas.create_polygon(points, width=2, outline='green2', fill=color1)  
    
        new_points = []
        for i in points:
            new_point = self.rotate([x, y], i, math.pi/5)
            new_points.append(new_point)
        self.canvas.create_polygon(new_points, width=2, outline='yellow', fill=color2)  
    

    def star_fractals(self, x, y, r, color1, color2):
        depth = int(self.depth.get())
        if depth>8: 
            pass 
        if r<400/(2.62**(depth-1)):
            return
        if r < 400/(2.62**(depth-1))-1:
            return
        
        else:
            self.simple_star(x, y, r, color1, color2)
            
            return self.star_fractals(x, y, r*1/2.62, color2, color1)

      
    def zoomin(self):
            self.r *= 2
            
            self.display()

    def zoomout (self):
            self.r/=2
            
            self.display()


    def display(self):
        self.canvas.delete("all")
        self.star_fractals(450, 450, self.r, "white",self.color.get())
        
     
Main()
