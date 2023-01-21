from tkinter import *
from tkvideo import tkvideo

w= Tk()
w.title("Tawad's angels video player")

lbltest = Label(w,text="Hello there",bg="black",fg="white").place(x=560,y=400)
lblVideo= Label(w)
lblVideo.pack()

player=tkvideo("C:\\Users\\tawad\\Git\\Fucked-Fractals\\y2meta.com - NASA _ The Big Bang.mp4",
                lblVideo,
                loop=1,
                size=(700,500))


player.play()
w.mainloop()