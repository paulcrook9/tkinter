# Import Module


# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry (widthxheight)
window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# root.resizable(False, False)
# root.attributes('-alpha', 0.5)

# root.iconbitmap('./icon.ico')

#adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)

# button is clicked
def clicked():

    res = "You wrote " + txt.get()
    lbl.configure(text = res)

#   lbl.configure(text = "I just got clicked")

# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,
           fg = "red", command=clicked)
# set Button grid
btn.grid(column=2, row=0)

# all widgets will be here
# Execute Tkinter
root.mainloop()