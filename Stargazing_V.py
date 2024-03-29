from tkinter import *
from tkvideo import *
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
        self.switch_Canvas(BeginningPage) #the program starts with the Main Canvas

    #Creating a function, that helps switching Canvases
    def switch_Canvas(self, Canvas_class):

        if self._mainCanvas:
            self._mainCanvas.pack_forget() #maincanvas is a variable, whose job is to store the currently dispayed canvas/page(class)

        canvas = Canvas_class(self) #here we assign the page that we want to be displayed to the variable canvas

        canvas.pack(fill="both", expand=True) #here we display the currently chosen canvas
        self._mainCanvas = canvas #here we assign the canvas to the maincanvas variable, aka the newly displayed page is being assigned

#Creating the Beginning Page
class BeginningPage(Canvas):
    def __init__(self, master, *args, **kwargs):
        
        #Initialising the canvaas
        Canvas.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self, bg = 'black')
        self.canvas.pack(fill="both", expand=True)

        #Message and Button
        self.info_for_the_user = Message(self.canvas, width = 300, bg = "black", font= ("Arial", 15), justify = "center", fg="white", text="An old prophecy goes:\n  \n \"...In the Beginning, There Was Nothing. \n  \n The Lord Said, ‘Let There Be Light.’ \n  \n Then There Was Still Nothing,\n  \n But when the User preessed the button, light appeared and our universe began...\"")
        self.info_for_the_user.place( x = 820, y = 100)

        Button(self.canvas, text="Light",
            command=lambda: master.switch_Canvas(VideoPage)).place(x = 560, y = 400)

#Creating the Video Page
class VideoPage(Canvas):
    def __init__(self, master, *args, **kwargs):
        
        #Initialising the canvaas
        Canvas.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self, bg = 'black')
        self.canvas.pack(fill="both", expand=True)

        self.backgroundimg = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\nightsky.png") #the code is made from Macbook, so the path for Windows users will be different
        self.canvas.create_image(0,0,image=self.backgroundimg, anchor = "nw")

        #Message and Button

        Button(self.canvas, text="Next",
            command=lambda: master.switch_Canvas(MainPage)).place(anchor="n",x = 980, y = 10)

        lblVideo= Label(self.canvas)
        lblVideo.place(anchor="center",x=560,y=400)

        player=tkvideo("C:\\Users\\tawad\\Git\\Fucked-Fractals\\y2meta.com - NASA _ The Big Bang.mp4",
                lblVideo,
                loop=1,
                size=(760,600))
        
        player.play()

#Creating the Main Page
class MainPage(Canvas):
    def __init__(self, master, *args, **kwargs):
        Canvas.__init__(self, master, *args, **kwargs)

        #Creating the Canvas and customizing it
        self.canvas = Canvas(self)
        self.canvas.pack(fill="both", expand=True)

        #Here we create the pictures, which will be used in the Main Page
        self.backgroundimg = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\nightsky.png") #the code is made from Macbook, so the path for Windows users will be different
        self.canvas.create_image(0,0,image=self.backgroundimg, anchor = "nw")
        #Canis Major Constellation
        self.imgcon = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\canis major.png") 
        self.canvas.create_image(30,0,image=self.imgcon, anchor = "nw")
        Label(self.canvas, 
            text = "Canis Major", bg = "black", fg="white").place(x = 26, y = 39)
        #Ursa Major Constellation
        self.imgcon1 = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\ursa major.png") 
        self.canvas.create_image(10,370,image=self.imgcon1, anchor = "nw")
        Label(self.canvas, 
            text = "Ursa Major", bg = "black", fg="white").place(x = 405, y = 690)
        #Pisces Constellation
        self.imgcon2 = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\pisces.png") 
        self.canvas.create_image(370,40,image=self.imgcon2, anchor = "nw")
        Label(self.canvas, 
            text = "Pisces", bg = "black", fg="white").place(x = 635, y = 70)
        #Orion Constellation
        self.imgcon3 = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\orion.png")
        self.canvas.create_image(480,280,image=self.imgcon3, anchor = "nw")
        Label(self.canvas, 
            text = "Orion", bg = "black", fg="white").place(x = 715, y = 450)


        #Creating the binding for 1-st constellation - Canis Major
        #our group has already figured out the position of the 1-st constellation in our program, which is within a recktangle, located between the 74th - 288th pixels for the range of x, and 50 - 322 pixels for the range of y
        x_of_1st_con = [] #here we are preserving the coordinates of the x range in which the 1-st constellation is located inside of
        y_of_1st_con = [] #here we are preserving the coordinates of the y range in which the 1-st constellation is located inside of
        for x in range (74, 289): #we use for-loop, because we want to exploit the computers labour, and not the human one, so each x of the x-axis range of the 1-st constellation is added into the list x_of_1st_con
            x_of_1st_con.append(x)
        for y in range (50, 323): #we do the same for each y of the y-axis range of the 1-st constelation, which are added to y_of_1st_con
            y_of_1st_con.append(y)

        #Creating the binding for 2-nd constellation - Ursa Major
        #the 2-nd constellation has a scope: from 27th - 524th pixel for the range of x, and from 383rd - 759th pixel for the range of y
        x_of_2nd_con = [] 
        y_of_2nd_con = [] 
        for x in range (27, 525): 
            x_of_2nd_con.append(x)
        for y in range (383, 760): 
            y_of_2nd_con.append(y)

        #Creating the binding for 3-rd constellation - Pisces
        #the 3-rd constellation has a scope: from 396th - 717th pixel for the range of x, and from 72nd - 320th pixel for the range of y 
        x_of_3rd_con = [] 
        y_of_3rd_con = [] 
        for x in range (396, 718): 
            x_of_3rd_con.append(x)
        for y in range (72, 321): 
            y_of_3rd_con.append(y)

        #Creating the binding for 4-th constellation - Orion
        #the 4-th constellation has a scope: from 570th - 811st pixel for the range of x, and from 351st - 726th pixel for the range of y 
        x_of_4th_con = [] 
        y_of_4th_con = [] 
        for x in range (570, 812): 
            x_of_4th_con.append(x)
        for y in range (351, 727): 
            y_of_4th_con.append(y)

        #We need a function to pass to the binding, and check if the coordinates of the point where the user clicks match with any of the constellation ones, which are stored in each list
        def checking(event):  
            if event.x in x_of_1st_con and event.y in y_of_1st_con: 
                master.switch_Canvas(FractalPage1) #here if the coordinates belongg to the ones in the list, if the result is True in other words, the canvas is changed
            elif event.x in x_of_2nd_con and event.y in y_of_2nd_con: 
                master.switch_Canvas(FractalPage1)
            elif event.x in x_of_3rd_con and event.y in y_of_3rd_con: 
                master.switch_Canvas(FractalPage1)
            elif event.x in x_of_4th_con and event.y in y_of_4th_con: 
                master.switch_Canvas(FractalPage1)
            else:
                pass
        self.canvas.bind("<Button>", checking)

        reseruniversebutton = Button(self.canvas, text = "Reset Universe", command=lambda: master.switch_Canvas(BeginningPage))
        reseruniversebutton.place(x = 990, y = 700)

        #Message
        self.info_for_the_user = Message(self.canvas, width = 271, bg = "#34495E", font= ("Arial", 12), justify = "center", fg="white", text="Did you know that in 1922, the International Astronomical Union (IAU) officially recognised 88 constellations, 48 of which were recorded by the Greek astronomer Ptolemy in his book ‘Almagest’ written around 150 AD. \n Many of them have very interesting and ancient stories, mostly derived from myths and legends. \n  \n According to a legend the Pisces constellation is composed of two fish who are connected together by a ribbon. The fish are the goddess Aphrodite and her son Eros (Roman: Venus and Cupid). They turned themselves into fish in order to escape from the monster Typhon. They then connected themselves together with a ribbon in order not to be separated. The constellation is located in an area of the sky known as \”the Sea\” or \”the Water\”, which is full of water related constellations. Pisces contains only faint stars, the stars however do seem to form two small circlets connected together by a string. The constellation is southeast of Pegasus, located between Aquarius and Aries, making it also one of the most difficult to see. \n  \n Please, select a constellation by clicking on it to learn more information.")
        self.info_for_the_user.place( x = 890, y = 70)

#Creating the First Fractal Page
class FractalPage1(Canvas):
    def __init__(self, master, *args, **kwargs):
        
        #Initialising the canvaas
        Canvas.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self)
        self.canvas.pack(fill="both", expand=True)
        self.r = 400 # added variable to keep track of the current radius
        #Background Photo
        self.bgimg = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\nightsky.png")
        self.canvas.create_image(0,0,image=self.bgimg, anchor = "nw")

        #Label, Entry, Buttons
        Label(self.canvas, 
            text = "Depth of the star: ", bg = "black", fg="white").place(anchor = "n", x = 450, y = 13)
        
        self.depth = StringVar(self.canvas)

        #The entry is used so the user can input the number of iterations, that they want to see.
        Entry(self.canvas, textvariable = self.depth, 
            justify = RIGHT).place(anchor = "n", x = 600, y = 10)

        Label(self.canvas, text = "Enter the color of star: ", bg="black", fg="white").place(anchor = "n", x = 100, y = 13)
        
        self.color = StringVar()

        Entry(self.canvas, textvariable = self.color, 
            justify = RIGHT).place(anchor= "n", x= 250, y=10)

        Button(self.canvas, text = "Display Recursive Star", 
            command = self.display).place(anchor = "n", x = 790, y = 10)

        Button(self.canvas, text="Main page",
            command=lambda: master.switch_Canvas(MainPage)).place(anchor = "se", x = 1087, y = 770)
        
        zoom_in_button = Button(self.canvas, text="Zoom in", command=self.zoomin, padx=10,pady=10)
        zoom_in_button.place(anchor = "n", x = 960, y = 10)
        zoom_out_button = Button(self.canvas, text="Zoom out", command=self.zoomout, padx=10,pady=10)
        zoom_out_button.place(anchor = "n", x = 1100, y = 10)

        #Learning Information
        self.learninginfo = Message(self.canvas, width = 250, bg = "#34495E", fg="white", justify = "center", pady = "15", padx = "10", font= ("Arial", 12),
            text  = "Why are stars drawn with 5 points? \n Have you ever wondered why are stars drawn with five points, while in reality they look barely anything alike? \n Well, this has something to do with light behaviour. Light establishes itself as both a wave and a particle. Sometimes, it behaves like a particle (known as a photon) and is thus able to travel in straight paths, but at other times, it travels like a wave. Although it doesn’t make much sense to us intuitively, there is conclusive evidence for light’s duality, named by scientists as the “wave-particle duality of light”. Thanks to these wave-like characteristics, when light emitted from a distant object reaches another object or opening, its waves are bounced or bent slightly around the object and interfere with each other to produce various patterns on whatever they ultimately fall on. This is the reason why any light source appears to sparkle with pointed corners when you squint your eyes.")
        self.learninginfo.place(anchor= "e", x = 1170, y = 400)


    # Natalia's Fractal
    # Creating a function that rotates the star         
    def rotate(self, origin, point, angle):
        ox, oy = origin
        px, py = point
    
        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        
        return [qx, qy]
    
    #Constructing a star (one layer of the fractal)
    # defining the points that connect/create a star shape and creating second star that is rotated by 72 degrees 
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
    
    #Creating the fractal (repeting the patern)
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
            self.delete("all")
            self.backgroundimg = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\nightsky.png") #the code is made from Macbook, so the path for Windows users will be different
            self.canvas.create_image(0,0,image=self.backgroundimg, anchor = "nw")
            self.display()

    def zoomout (self):
            self.r/=2
            self.delete("all")
            self.backgroundimg = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\nightsky.png") #the code is made from Macbook, so the path for Windows users will be different
            self.canvas.create_image(0,0,image=self.backgroundimg, anchor = "nw")
            self.display()

    #Displaying the created fractal        
    def display(self):
        self.canvas.delete("all")
        self.backgroundimg = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\nightsky.png") #the code is made from Macbook, so the path for Windows users will be different
        self.canvas.create_image(0,0,image=self.backgroundimg, anchor = "nw")
        self.star_fractals(450, 450, self.r, "",self.color.get())


#Creating the Second Fractal Page (Michas fractal), which is left unused
"""
class FractalPage2(Canvas):
    def __init__(self, master, *args, **kwargs):
        
        #Initialising the canvaas
        Canvas.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self)
        self.canvas.pack(fill="both", expand=True)

        #Background Photo
        self.bgimg = PhotoImage(file="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\nightsky.png")
        self.canvas.create_image(0,0,image=self.bgimg, anchor = "nw")

        Button(self.canvas, text="Main page",
            command=lambda: master.switch_Canvas(MainPage)).place(anchor = "se", x = 1087, y = 770)
    
        
        Label(self.canvas, text = "Depth of the star: ", bg = "black", fg="white").place(anchor = "n", x = 420, y = 13)
        
        self.depth = StringVar(self.canvas)

        #The entry is used so the user can input the number of iterations, that they want to see.
        Entry(self.canvas, textvariable = self.depth, 
            justify = RIGHT).place(anchor = "n", x = 600, y = 10)

        Button(self.canvas, text = "Display Recursive Star: ", 
            command = self.display()).place(anchor = "n", x = 790, y = 10)
        
        Label(self.canvas, text = "input position on the X axis: ", bg = "black", fg="white").place(anchor = "n", x = 760, y = 13)
        
        self.input_x = StringVar(self.canvas)

        #The entry is used so the user can input the position on x axis, that they want to see.
        Entry(self.canvas, textvariable = self.input_x, 
            justify = RIGHT).place(anchor = "n", x = 890, y = 10)

    
    #Michas fractal
    input_iterations = 20
    input_x = int(input("input position on x axis: ")) * 10
    input_y = int(input("input position on y axis: ")) * 10

    # Set size and position of the star

    size = input_iterations
    x = input_x
    y = input_y

    # Define a recursive function to draw the star
    def draw_star(self,size, x, y):
        # Base case: if the size is too small, stop recursing
        if size < 1:
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
        self.canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, fill="orange", outline="yellow")

        # Recursively draw smaller stars
        self.draw_star(size / 3, x, y - size / 3)
        self.draw_star(size / 3, x + size - size / 3, y)
        self.draw_star(size / 3, x, y + size / 3)
        self.draw_star(size / 3, x - size + size / 3, y)

    # Initial call to draw the star
    def display(self):
        self.canvas.delete("all")
        self.draw_star(450, 450, self.r, "white",self.color.get())
"""

if __name__ == "__main__":
    app = ProgramEngine()
    app.mainloop()