from chuck import *
from tkinter import *

root = Tk()
fast = None
instruments = { "mandolin": 0, 
                "voice": 0, 
                "saxophone": 0, 
                "shaker": 0, 
                "sitar": 0, 
                "moog": 0,
                "struckbar": 0,
                "bowed": 0,
                "blowhole": 0 }

# make functions for what to do when the buttons are pressed
def clickFast():
    false = True
    print(false)

def clickSlow():
    false = False
    print(false)

def clickPrintInstruments():
    for instrument, val in instruments.items():
        print(instrument, val.get())


for instrument in instruments.keys():
    checked = IntVar()
    checkbox = Checkbutton(root, text=instrument, variable = checked)
    checkbox.pack()
    instruments[instrument] = checked

# make speed buttons for the GUI 
fast_button = Button(root, text="fast!", command=clickFast)
slow_button = Button(root, text="slowww", command=clickSlow)

fast_button.pack()
slow_button.pack()

# debugging button to make sure the checkbox values are being taken
print_instruments_button = Button(root, text="Print which instruments have been selected", command=clickPrintInstruments)
print_instruments_button.pack()

root.mainloop()

# disable the buttons once the person clicks the "GENERATE MUSIC" button



init()

