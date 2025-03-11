from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from random import *


class Combat_Window(Tk):
    def __init__(self, chosen):
        super().__init__()
        self.chosen = list(chosen)
        self.position = 0

        self.top_canvas = Canvas(self,width=600,height=100)
        self.top_canvas.grid_propagate(False)
        self.top_canvas.grid(column=0,row=0,columnspan=10,pady=2)
        self.top_scroll = Scrollbar(self,orient="horizontal",command=self.top_canvas.xview)
        self.top_scroll.grid(column=0,row=1,columnspan=10)
        self.top_canvas.config(xscrollcommand=self.top_scroll.set)
        

        self.nxcanvas = Canvas(self,width=45,height=100)
        self.nxcanvas.grid(column=10,row=1)
        self.nxcanvas.grid_propagate(False)
        self.next_round_b = Button(self.nxcanvas,text = "Next Round",command=self.next_round)
        self.next_round_b.pack()        
        self.next_round()

    # Fucntion that clears the initiative track and shuffles the combatants for a new round.
    def next_round(self):
        self.clear_init_track()
        shuffle(self.chosen)
        self.rebuild_track()
        

    #Function to clear the iniative track.
    def clear_init_track(self):
        for widget in self.top_canvas.winfo_children():
            widget.destroy()


    def move_left(self,chosen_item):
        index = self.chosen.index(chosen_item)
        if index > 0:  # Ensure it's not the first item
        # Swap positions of the chosen item and the one to its left
            self.chosen[index], self.chosen[index - 1] = self.chosen[index - 1], self.chosen[index]
        # Refresh the initiative track
            self.clear_init_track()
            self.rebuild_track()


    def move_right(self,chosen_item):
        index = self.chosen.index(chosen_item)
        if index < len(self.chosen) - 1:  # Ensure it's not the first item
        # Swap positions of the chosen item and the one to its left
            self.chosen[index], self.chosen[index + 1] = self.chosen[index + 1], self.chosen[index]
        # Refresh the initiative track
            self.clear_init_track()
            self.rebuild_track()


    def rebuild_track(self):
        for chose in self.chosen:            
            item_frame = Frame(self.top_canvas)
            item_frame.grid(column=self.position,row=1,padx=5,pady=5)
            combatant = Button(item_frame,text = chose)
            combatant.pack()
            remove_button = Button(item_frame,text="Remove",command=lambda chosen_item=chose, frame=item_frame:(
                self.chosen.remove(chosen_item),
                frame.destroy()
            ))
            remove_button.pack(padx=5)
            left_button = Button(item_frame,text="<",command=lambda chosen_item=chose: self.move_left(chosen_item))
            left_button.pack(side="left",padx=5)
            right_button = Button(item_frame,text=">",command=lambda chosen_item=chose: self.move_right(chosen_item))
            right_button.pack(side="right",padx=5)

            self.top_canvas.config(scrollregion=self.top_canvas.bbox("all"))
            print(self.top_canvas.bbox("all"))

            self.position += 1
        self.position = 0

        
        