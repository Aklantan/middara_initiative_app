import tkinter.messagebox
from tkinter import *
import random
#import pyperclip
import json


# -------------------- Variables ----------------------------------------#
#
#

options = [ 
    "Nightingale",
    "Remi",
    "Rook",
    "Zeke"
] 




# ---------------------------- UI SETUP ------------------------------- #
#Create Main Window
#
main_window = Tk()
main_window.title("Middara Iniative App")
main_window.config(pady=50, padx=50)

clicked = StringVar()


#Create lower Frame
low_frame = Frame(height  = 100, width = 200, borderwidth=1, relief= "solid", padx=20, pady=20)
low_frame.grid(row = 1, column = 1, columnspan = 3)
bottom_frame = Frame(height  = 100, width = 200, borderwidth=1, relief= "solid", padx=20, pady=20)
bottom_frame.grid(row = 2, column = 1, columnspan = 3)
right_frame = Frame(height  = 300, width = 200, borderwidth=1, relief= "solid", padx=20, pady=20)
right_frame.grid(row = 1, column = 5, rowspan = 3)

#create buttons
gen_iniative = Button(low_frame,text = "Add Character ",  height=1)
gen_iniative.grid(row = 1 , column = 3)

save_pass = Button(bottom_frame, text = "Roll Iniative", height=1, width =36)
save_pass.grid(row = 3, column =1, columnspan =2 )


#create entry lines


enter_user = OptionMenu(low_frame,clicked,*options)
enter_user.grid(row = 1, column =1, columnspan = 2)


# #Create Labels for entry lines
# website_label = Label(low_frame, text = "Website" , anchor="w")
# website_label.grid(row = 0, column = 0)






main_window.mainloop()