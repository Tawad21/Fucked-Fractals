import tkinter as tk
from time import *



root = tk.Tk()
root.geometry("550x550")

canvas = tk.Canvas(root,bg="#FFFFFF",height=200)
canvas.pack(fill = tk.X, padx = 20, pady = 5)

root.mainloop()