from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from random import *


class Combat_Window(Tk):
    def __init__(self, chosen):
        super().__init__()
        self.chosen = list(chosen)
        self.position = 0

        self.top_frame = Frame(self)
        self.top_frame.grid(column=0,row=0,columnspan=10,pady=2)

        self.nxframe = Frame(self)
        self.nxframe.grid(column=10,row=1)
        self.next_round_b = Button(self.nxframe,text = "Next Round",command=self.next_round)
        self.next_round_b.pack()        
        self.next_round()

    # Fucntion that clears the initiative track and shuffles the combatants for a new round.
    def next_round(self):
        self.clear_init_track()
        shuffle(self.chosen)
        
        for chose in self.chosen:            
            item_frame = Frame(self.top_frame)
            item_frame.grid(column=self.position,row=1,padx=5,pady=5)
            combatant = Button(item_frame,text = chose)
            combatant.pack()
            remove_button = Button(item_frame,text="Remove",command=item_frame.destroy)
            remove_button.pack(side="right",padx=5)
            self.position += 1
        self.position = 0

    #Function to clear the iniative track.
    def clear_init_track(self):
        for widget in self.top_frame.winfo_children():
            widget.destroy()

        
        