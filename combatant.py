from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk


class Combat_Window(Tk):
    def __init__(self, chosen):
        super().__init__()
        self.chosen = chosen
        self.position = 0

        self.top_frame = Frame(self)
        self.top_frame.grid(column=0,row=0,columnspan=10,pady=2)

        for chose in self.chosen:
            item_frame = Frame(self.top_frame)
            item_frame.grid(column=self.position,row=1,padx=5,pady=5)
            combatant = Button(item_frame,text = chose)
            combatant.pack()
            self.position += 1
        self.position = 0





        
        