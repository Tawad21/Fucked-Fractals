import tkinter as tk
import NatsFractalInterface

root = tk.Tk()

#region calculations and window
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

root.title('consellsation')

# Add image file
bg = tk.PhotoImage(file = "C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\Backgroundimg.png")
sb = tk.PhotoImage(file ="C:\\Users\\tawad\\Git\\Fucked-Fractals\\img\\sidebar.png")
#endregion



#region functions

# Frame for side bar
options_frame = tk.Frame(root, bg='#101B29',highlightbackground='black',highlightthickness='2')

side_img = tk.Label(options_frame, image=sb)
side_img.pack()

# 
def hide_indicators():
    home_indicate.config(bg='#101B29')
    page1_indicate.config(bg='#101B29')
    page2_indicate.config(bg='#101B29')
    page3_indicate.config(bg='#101B29')

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='white')
    page()

def home_page():
    home_frame = tk.Frame(main_frame)
    label1 = tk.Label( home_frame, image = bg)
    #label1.place(x = 0, y = 0)
    label1.pack()
    home_frame.pack()

def page1_page():
    page1_frame = tk.Frame(main_frame)
    label1 = tk.Label( page1_frame, image = bg)
    #label1.place(x = 0, y = 0)
    label1.pack()
    page1_frame.pack()

def page2_page():
    page2_frame = tk.Frame(main_frame)
    label1 = tk.Label(page2_frame, image = bg)
    #label1.place(x = 0, y = 0)
    label1.pack()
    page2_frame.pack()

def page3_page():
    page3_frame = tk.Frame(main_frame)
    label1 = tk.Label( page3_frame, image = bg)
    #label1.place(x = 0, y = 0)
    label1.pack()
    page3_frame.pack()

#endregion 

#region buttons
home_btn = tk.Button(options_frame, text='Home', font=('Bold',15), 
                    fg='white',bd=0,bg='#101B29',command=lambda: indicate(home_indicate, home_page()))
home_btn.place(x=60, y=50)
home_indicate = tk.Label(options_frame, text='', bg='#101B29')
home_indicate.place(x=3, y=50, width=5, height=40)

page1_btn = tk.Button(options_frame, text='Page 1', font=('Bold',15),
                    fg='white',bd=0,bg='#101B29',command=lambda: indicate(page1_indicate, page1_page(), NatsFractalInterface.Main()))
page1_btn.place(x=60, y=100)
page1_indicate = tk.Label(options_frame, text='', bg='#101B29')
page1_indicate.place(x=3, y=100, width=5, height=40)

page2_btn = tk.Button(options_frame, text='Page 2', font=('Bold',15), 
                    fg='white',bd=0,bg='#101B29',command=lambda: indicate(page2_indicate, page2_page()))
page2_btn.place(x=60, y=150)
page2_indicate = tk.Label(options_frame, text='', bg='#101B29')
page2_indicate.place(x=3, y=150, width=5, height=40)

page3_btn = tk.Button(options_frame, text='Page 3', font=('Bold',15), 
                    fg='white',bd=0,bg='#101B29',command=lambda: indicate(page3_indicate, page3_page()))
page3_btn.place(x=60, y=200)
page3_indicate = tk.Label(options_frame, text='', bg='#101B29')
page3_indicate.place(x=3, y=200, width=5, height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=200,height=600)
#endregion

#side_img = tk.Label(options_frame, image=sb)
#side_img.pack()

#region mainframe
main_frame = tk.Frame(root)
main_img = tk.Label(main_frame, image = bg)
main_img.pack()
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=880,height=600)

#endregion

root.mainloop()