import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import random
#import pyperclip
import json
from combatant import Combat_Window
from PIL import Image,ImageTk


# -------------------- Variables ----------------------------------------#
#
#

options = [ 
    "Nightingale",
    "Remi",
    "Rook",
    "Zeke"
] 

chosen = set()





#--------------------- Functions ----------------------------------------#
#
#

# Function to take the value of the combobox and add it to the right frame with a corresponding Remove button.

def add_character():
    item_frame = Frame(right_canvas)
    item_frame.pack(pady=2)

    chosen.add(clicked.get())

    label = Label(item_frame, text = clicked.get())
    label.pack(side="left",padx=5)

    remove_button = Button(item_frame,text="Remove",command=item_frame.destroy)
    remove_button.pack(side="right",padx=5)


#Function to open the combat window and move to the next stage of the application.

def roll_iniative():
    combat_window = Combat_Window(chosen)
    combat_window.title("Combat")
    combat_window.geometry("1080x860")






# ---------------------------- UI SETUP ------------------------------- #
#Create Main Window
#
main_window = Tk()
main_window.title("Middara Iniative App")
main_window.resizable(0,0)
main_window.geometry("600x600")
main_window.grid_propagate(False)
main_window.config(pady=50, padx=50)

clicked = StringVar()
style = Style()
style.configure("FRAME")


#Create Frames
top_canvas = Canvas(height  = 100, width = 200)
top_canvas.grid_propagate(False)
top_canvas.grid(row=0,column=1,columnspan=4)
low_canvas = Canvas(height  = 100, width = 350)
low_canvas.grid_propagate(False)
low_canvas.grid(row = 1, column = 1, columnspan = 3)
bottom_canvas = Canvas(height  = 100, width = 300)
bottom_canvas.grid_propagate(False)
bottom_canvas.grid(row = 2, column = 1, columnspan = 3)
right_canvas = Canvas(height  = 300, width = 200)
right_canvas.grid_propagate(False)
right_canvas.grid(row = 1, column = 4, rowspan = 3)


#Put Middara Logo at top
image = Image.open("assets/middarralogo.png")
resize_img = image.resize((300,200))
tk_img = ImageTk.PhotoImage(resize_img)
image_label = Label(top_canvas,image=tk_img)
image_label.pack()

#create buttons
gen_iniative = Button(low_canvas,text = "Add Character ",command=add_character)
gen_iniative.grid(row = 1 , column = 3)

save_pass = Button(bottom_canvas, text = "Roll Iniative",command=roll_iniative)
save_pass.place(x=130,y=40 )


#create entry lines


enter_user = Combobox(low_canvas,textvariable=clicked,values=options)
enter_user.grid(row = 1, column =1, columnspan = 1)


# #Create Labels for entry lines
# website_label = Label(low_frame, text = "Website" , anchor="w")
# website_label.grid(row = 0, column = 0)






main_window.mainloop()