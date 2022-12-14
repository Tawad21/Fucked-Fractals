from tkinter import *
import re
import math

#First of all, we need the engine of our program, so we're creating it before everything else
class ProgramEngine(Tk):
    #Initialising the program
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1200x1080")
        self.title("Stargazing")
        self._mainCanvas= None
        self._allCanvases = dict()
        self.switch_Canvas(MainPage)

    #Creating a function, that helps switching Canvases
    def switch_Canvas(self, Canvas_class):

        if self._mainCanvas:
            self._mainCanvas.pack_forget()

        canvas = self._allCanvases.get(Canvas_class, False)

        if not canvas:
            canvas = Canvas_class(self)
            self._allCanvases[Canvas_class] = canvas

        canvas.pack(fill="both", expand=True)
        self._mainCanvas = canvas

#Creating the Main Page
class MainPage(Canvas):
    def __init__(self, master, *args, **kwargs):
        Canvas.__init__(self, master, *args, **kwargs)

        #Creating the Canvas and customizing it
        self.canvas = Canvas(self)

        self.backgroundimg = PhotoImage(file="/Users/vladimirpetkov/Desktop/school/project fractals/nightsky.png") #the code is made from Macbook, so the path for Windows users will be different
        self.canvas.create_image(0,0,image=self.backgroundimg, anchor = "nw")

        self.canvas.pack(fill="both", expand=True)

        #Message
        self.welcome_message = Message(self.canvas, width = 200, bg = "#34495E", font= ("Arial", 16), justify = "center", text="Welcome to Tawad's Angels' Stargazing! \n Unfortunately, we're still in progress... ")
        self.welcome_message.place(anchor = "n", x = 600, y = 10)

        #Button that sends the user to the Fractal Page
        Button(self.canvas, text="Fractal N1 ",
              command=lambda: master.switch_Canvas(FractalPage)).place(anchor = "n", x = 600, y = 120)

#Creating the Fractal Page
class FractalPage(Canvas):
    def __init__(self, master, *args, **kwargs):
        
        #Initialising the canvaas
        Canvas.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self, width=900, height=900)

        #Background Photo
        self.bgimg = PhotoImage(file="/Users/vladimirpetkov/Desktop/school/project fractals/nightsky.png")
        self.canvas.create_image(0,0,image=self.bgimg, anchor = "nw")

        #Label, Entry, Buttons
        Label(self.canvas, 
            text = "Depth of the star: ", bg = "black").place(anchor = "n", x = 420, y = 13)
        self.depth = StringVar(self.canvas)

        #The entry is used so the user can input the number of iterations, that they want to see.
        Entry(self.canvas, textvariable = self.depth, 
            justify = RIGHT, bg="black").place(anchor = "n", x = 600, y = 10)

        Button(self.canvas, text = "Display Recursive Star", 
            command = self.display).place(anchor = "n", x = 790, y = 10)

        Button(self.canvas, text="Main page",
            command=lambda: master.switch_Canvas(MainPage)).place(anchor = "se", x = 1087, y = 770)
        
        #Learning Information
        self.learninginfo = Message(self.canvas, width = 250, bg = "#34495E", justify = "center", pady = "15", padx = "10", font= ("Arial", 15),
            text  = "Why are stars drawn with 5 points? \n Have you ever wondered why are stars drawn with five points, while in reality they look barely anything alike? \n Well, this has something to do with light behaviour. Light establishes itself as both a wave and a particle. Sometimes, it behaves like a particle (known as a photon) and is thus able to travel in straight paths, but at other times, it travels like a wave. Although it doesn’t make much sense to us intuitively, there is conclusive evidence for light’s duality, named by scientists as the “wave-particle duality of light”. Thanks to these wave-like characteristics, when light emitted from a distant object reaches another object or opening, its waves are bounced or bent slightly around the object and interfere with each other to produce various patterns on whatever they ultimately fall on. This is the reason why any light source appears to sparkle with pointed corners when you squint your eyes.")
        self.learninginfo.place(anchor= "e", x = 1170, y = 400)

        self.canvas.pack(fill="both", expand=True)


    # Natalia's Fractal
    # Creating a function that rotates the star         
    def rotate(self, origin, point, angle):
        ox, oy = origin
        px, py = point
    
        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        
        return [qx, qy]
    
    #Constructing a star (one layer of the fractal)
    def simple_star(self, x, y, r, color1, color2):
        a = [x-int(r*math.sin(2*math.pi/5)), y-int(r*math.cos(2*math.pi/5))]
        b = [x+int(r*math.sin(2*math.pi/5)), y-int(r*math.cos(2*math.pi/5))]
        c = [x-int(r*math.sin(math.pi/5)), y+int(r*math.cos(math.pi/5))]
        d = [x, y-r]
        e = [x+int(r*math.sin(math.pi/5)), y+int(r*math.cos(math.pi/5))]
        points = [a, b, c, d, e, a]
        
        self.canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline='#FAFAD2', fill = "black")
        self.canvas.create_polygon(points, width=2, outline='#FFE4B5', fill=color1)  
    
        new_points = []
        for i in points:
            new_point = self.rotate([x, y], i, math.pi/5)
            new_points.append(new_point)
        self.canvas.create_polygon(new_points, width=2, outline='#FAFAD2', fill=color2)  
    
    #Creating the fractal (repeting the patern)
    def star_fractals(self, x, y, r, color1, color2):
        depth = int(self.depth.get())

        if r < 400/(2.62**(depth-1))-1:
            return
        
        else:
            self.simple_star(x, y, r, color1, color2)
            return self.star_fractals(x, y, r*1/2.62, color2, color1)
    
    #Displaying the created fractal        
    def display(self):
        self.star_fractals(450, 450, 400, '#4682B4', '#FF4500')



if __name__ == "__main__":
    app = ProgramEngine()
    app.mainloop()