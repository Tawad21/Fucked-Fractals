import tkinter as tk

root = tk.Tk()

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

options_frame = tk.Frame(root, bg='#c3c3c3',highlightbackground='black',highlightthickness='2')

home_btn = tk.Button(options_frame, text='Home', font=('Bold',15), fg='#158aff',bd=0,bg='#c3c3c3')
home_btn.place(x=60, y=50)

home_indicATE = tk.Label(options_frame, text='')

page1_btn = tk.Button(options_frame, text='Page 1', font=('Bold',15), fg='#158aff',bd=0,bg='#c3c3c3')
page1_btn.place(x=60, y=100)

page2_btn = tk.Button(options_frame, text='Page 2', font=('Bold',15), fg='#158aff',bd=0,bg='#c3c3c3')
page2_btn.place(x=60, y=150)

page3_btn = tk.Button(options_frame, text='Page 3', font=('Bold',15), fg='#158aff',bd=0,bg='#c3c3c3')
page3_btn.place(x=60, y=200)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=200,height=600)

main_frame = tk.Frame(root)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=880,height=600)

root.mainloop()