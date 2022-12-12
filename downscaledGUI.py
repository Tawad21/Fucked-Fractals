
# Import module 
from tkinter import *
  
# Create object 
root = Tk()
  
# Adjust size 
window_width = 1080
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
  
# Add image file
bg = PhotoImage(file = "C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\Backgroundimg.png")
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
  
label2 = Label( root, text = "To the Stars")
label2.pack(pady = 50)
  
# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20)

# Add buttons
button1 = Button(frame1,text="Page One")
button1.pack(pady=20)
  
button2 = Button( frame1, text = "Page Two")
button2.pack(pady = 20)

button3 = Button( frame1, text = "Exit", command= lambda: root.quit())
button3.pack(pady = 20)
  
# Execute tkinter

root.mainloop()
