import tkinter as tk
from tkinter import ttk
import re
from PIL import Image, ImageTk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._mainCanvas= None
        # The dictionary to hold the class type to switch to
        # Each new class passed here, will only have instance or object associated with it (i.e the result of the Key)
        self._allCanvases = dict()
        # Switch (and create) the single instance of StartUpPage
        self.switch_Canvas(StartUpPage)

    def switch_Canvas(self, Canvas_class):

        # Unless the dictionary is empty, hide the current Frame (_mainCanvas is a frame)
        if self._mainCanvas:
            self._mainCanvas.pack_forget()

        # is the Class type passed one we have seen before?
        canvas = self._allCanvases.get(Canvas_class, False)

        # if Canvas_class is a new class type, canvas is False
        if not canvas:
            # Instantiate the new class
            canvas = Canvas_class(self)
            # Store it's type in the dictionary
            self._allCanvases[Canvas_class] = canvas

        # Pack the canvas or self._mainCanvas (these are all frames)
        canvas.pack(pady = 60)
        # and make it the 'default' or current one.
        self._mainCanvas = canvas

class StartUpPage(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)
        tk.Frame(self) # Here the parent of the frame is the self instance of type tk.Canvas
        tk.Label(self, text="Example").grid(column = 0, row = 0)
        self.canvas = tk.Canvas(self, )
        tk.Button(self, text="Canvas1",
              command=lambda: master.switch_Canvas(PageOne)).grid(column = 0, row = 1)
        tk.Button(self, text="Canvas2",
              command=lambda: master.switch_Canvas(PageTwo)).grid(column = 0, row = 2)


class PageOne(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self,master, *args, **kwargs)
        self.canvas = tk.Canvas(self,bg='blue', width=430)
        print('got',self,master,args,kwargs)
        tk.Label(self, text="First Canvas").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Back to start-up page",
              command=lambda: master.switch_Canvas(StartUpPage)).pack()

        self.canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

class PageTwo(tk.Frame): # Sub-lcassing tk.Frame
    def __init__(self, master, *args, **kwargs):
        # self is now an istance of tk.Frame
        tk.Frame.__init__(self,master, *args, **kwargs)
        # make a new Canvas whose parent is self.
        self.canvas = tk.Canvas(self,bg='yellow', width=430)
        self.label = tk.Label(self, text="Second Canvas").pack(side="top", fill="x", pady=5)
        self.button = tk.Button(self, text="Back to start-up page",
              command=lambda: master.switch_Canvas(StartUpPage))

        self.button.pack()
        # pack the canvas inside the self (frame).
        self.canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        #print('is instance',isinstance(self,tk.Frame))

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()