from chuck import *
from tkinter import *
import random

QUARTER_NOTE_DURATION = 0.5

root = Tk()
fast = None
instruments = { "mandolin1": 0, 
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
    root.quit()


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
init()

# disable the buttons once the person clicks the "GENERATE MUSIC" button

# instrument functions
mandolin = Mandolin()
voice = FMVoices()
sax = Saxophone()
shaker = Shakers()
sitar = Sitar()
moog = MoogSynthesizer()
struckbar = StruckBar()
bowed = Bowed()
blowhole = BlowHole()

def mtof(midi):
    a = 440 #frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((midi - 9) / 12))

# 2 octave C major scale
# make this into a dictionary
c_major_scale = [48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72]

# C3, C4, C5
c_roots = [48, 60, 72]

# F3, F4, F5
f_roots = [53, 65, 77]

# G3, G4, G5
g_roots = [55, 67, 79]

# intervals for common chords
major_third = [0, 4, 7]
minor_third = [0, 3, 7]
diminished = [0, 3, 6]
augmented = [0, 4, 8]

chord_types = [major_third, minor_third, diminished, augmented]

def play(instrument, midi_note, time, strength):
    instrument.connect()
    instrument.setFrequency(mtof(midi_note))
    instrument.noteOn(strength)
    wait(time)
    instrument.noteOff(1.0)

def playQuarter(instrument, strength):
    play(instrument, QUARTER_NOTE_DURATION, strength)

def playEighth(instrument, midi_note, strength):
    play(instrument, midi_note, QUARTER_NOTE_DURATION / 2, strength)

def playSixteenth(instrument, midi_note, strength):
    play(instrument, midi_note, QUARTER_NOTE_DURATION / 4, strength)

def playHalf(instrument, midi_note, strength):
    play(instrument, midi_note, 2 * QUARTER_NOTE_DURATION, strength)


# play(sax, 60, 10.0, 0.8)
# make base beat 
# pattern = []

# play(sax, 20.0, 1.0)
# beat is made up of 4 random instruments selected from the 
# shaker choices - 0 to 22

# 4 shaker preset numbers
shakers = [None] * 4 
for i in range(0, 4):
    preset_num = random.randint(0, 14)
    print(preset_num)
    shakers[i] = preset_num

pattern = []
# 4 shakers + rest
for i in range(0, 8):
    instr = random.randint(0, 4)
    print(instr)
    if instr == 4:
        pattern.append("REST")
    else:
        pattern.append(shakers[instr])

print(pattern)
current_step = 0

# loop this eventually 

def play_randomized_beat():
    for i in range(len(pattern)):
        if pattern[i] == "REST":
            wait(QUARTER_NOTE_DURATION)
        else:
            print(pattern[i])
            shaker.preset(pattern[i])
            play(shaker, 60, QUARTER_NOTE_DURATION, 1.0)

play_randomized_beat()

# shaker.preset(16)
# play(shaker, 60, QUARTER_NOTE_DURATION, 1.0)
# shaker.preset(1)
# play(shaker, 60, QUARTER_NOTE_DURATION, 1.0)

# first pick the four instruments and initialize them
# then make a pattern of 8 or 16 beats based on 
