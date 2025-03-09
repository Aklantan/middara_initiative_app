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
    item_frame = Frame(right_frame)
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
    combat_window.geometry("800x800")






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
top_frame = Frame(height  = 100, width = 200, relief= "solid",padding=20)
top_frame.grid(row=0,column=1,columnspan=4)
low_frame = Frame(height  = 100, width = 200, relief= "solid",padding=20)
low_frame.grid(row = 1, column = 1, columnspan = 3)
bottom_frame = Frame(height  = 100, width = 200, relief= "solid",padding = 20)
bottom_frame.grid(row = 2, column = 1, columnspan = 3)
right_frame = Frame(height  = 300, width = 200, borderwidth=1, relief= "solid", padding = 20)
right_frame.grid(row = 1, column = 4, rowspan = 3)


#Put Middara Logo at top
image = Image.open("assets/middarralogo.png")
resize_img = image.resize((300,200))
tk_img = ImageTk.PhotoImage(resize_img)
image_label = Label(top_frame,image=tk_img)
image_label.pack()

#create buttons
gen_iniative = Button(low_frame,text = "Add Character ",command=add_character)
gen_iniative.grid(row = 1 , column = 3)

save_pass = Button(bottom_frame, text = "Roll Iniative",command=roll_iniative)
save_pass.grid(row = 5, column =1, columnspan =2 )


#create entry lines


enter_user = Combobox(low_frame,textvariable=clicked,values=options)
enter_user.grid(row = 1, column =1, columnspan = 2)


# #Create Labels for entry lines
# website_label = Label(low_frame, text = "Website" , anchor="w")
# website_label.grid(row = 0, column = 0)






main_window.mainloop()