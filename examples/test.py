from chuck import *
from tkinter import *
import random

QUARTER_NOTE_DURATION = 0.5
SONG_DURATION = 12 * 4 * QUARTER_NOTE_DURATION

root = Tk()
fast = True
instruments = { "mandolin": 0, 
                "voice": 0, 
                "saxophone": 0, 
                "sitar": 0, 
                "moog": 0,
                "struckbar": 0,
                "bowed": 0,
                "blowhole": 0 }

# make functions for what to do when the buttons are pressed
def clickFast():
    global fast
    fast = True
    print(fast)

def clickSlow():
    global fast
    fast = False
    print(fast)

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
print_instruments_button = Button(root, text="Pick three instruments, and a song speed, then click this button!", command=clickPrintInstruments)
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

# 1 octave C major scale
# make this into a dictionary
c_major_scale = [60, 62, 64, 65, 67, 69, 71, 72]

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

print(fast)
if fast:
    QUARTER_NOTE_DURATION = 0.5
else:
    print("IN HERE")
    QUARTER_NOTE_DURATION = 1.0


print(QUARTER_NOTE_DURATION)

def play(instrument, midi_note, time, strength):
    instrument.connect()
    instrument.setFrequency(mtof(midi_note))
    if instrument is shaker or struckbar:
        instrument.setGain(0.8)
    elif instrument is mandolin or sax or blowhole:
        instrument.setGain(0.05)
    elif instrument is voice or sitar or moog or bowed:
        instrument.setGain(0.05)
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

# 4 shaker preset numbers
shakers = [None] * 4 
for i in range(0, 4):
    preset_num = random.randint(0, 14)
    shakers[i] = preset_num

pattern = []
# 4 shakers + rest
for i in range(0, 16):
    instr = random.randint(0, 4)
    if instr == 4:
        pattern.append("REST")
    else:
        pattern.append(shakers[instr])

current_step = 0

# pattern is always 2 measures of 16 eighth notes
# we need to loop pattern 6 times

def play_randomized_beat():
    for i in range(len(pattern * 3)):
        if pattern[i % len(pattern)] == "REST":
            wait(QUARTER_NOTE_DURATION / 2)
        else:
            shaker.preset(pattern[i % len(pattern)])
            play(shaker, 60, QUARTER_NOTE_DURATION / 2, 1.0)


# some logic to pick the instruments that the user wants
musical_phrase = []
for i in range(0, 12):
    musical_phrase.append(random.randint(0, len(c_major_scale) - 1))

def play_randomized_phrase(real_instrument):
    for i in range(len(musical_phrase)):
        print(c_major_scale[musical_phrase[i]])
        play(real_instrument, c_major_scale[musical_phrase[i]], QUARTER_NOTE_DURATION, 0.5)

# first pick the four instruments and initialize them
# then make a pattern of 8 or 16 beats based on 

def play_mandolin():
    check_and_wait("mandolin")
    play_randomized_phrase(mandolin)

def play_voice():
    check_and_wait("voice")
    play_randomized_phrase(voice)

def play_saxophone():
    check_and_wait("saxophone")
    play_randomized_phrase(sax)

def play_sitar():
    check_and_wait("sitar")
    play_randomized_phrase(sitar)

def play_moog():
    check_and_wait("moog")
    play_randomized_phrase(moog)

def play_struckbar():
    check_and_wait("struckbar")
    play_randomized_phrase(struckbar)

def play_bowed():
    check_and_wait("bowed")
    play_randomized_phrase(bowed)

def play_blowhole():
    check_and_wait("blowhole")
    play_randomized_phrase(blowhole)

selected_instruments = []
for instrument, val in instruments.items():
    if val.get() == 1:
        selected_instruments.append(instrument)

selected_instruments = selected_instruments[0:3]
instrument_funcs = [None] * 3

def check_and_wait(instr_str):
    for i in range(len(selected_instruments)):
        if selected_instruments[i] == instr_str and i == 1:
            wait(4*QUARTER_NOTE_DURATION)
        elif selected_instruments[i] == instr_str and i == 2:
            wait(8*QUARTER_NOTE_DURATION)

def pick_instrument():
    for i in range(len(selected_instruments)):
        if selected_instruments[i] == "mandolin":
            instrument_funcs[i] = play_mandolin
        elif selected_instruments[i] == "voice":
            instrument_funcs[i] = play_voice
        elif selected_instruments[i] == "saxophone":
            instrument_funcs[i] = play_saxophone
        elif selected_instruments[i] == "sitar":
            instrument_funcs[i] = play_sitar
        elif selected_instruments[i] == "moog":
            instrument_funcs[i] = play_moog
        elif selected_instruments[i] == "struckbar":
            instrument_funcs[i] = play_struckbar
        elif selected_instruments[i] == "bowed":
            instrument_funcs[i] = play_bowed
        elif selected_instruments[i] == "blowhole":
            instrument_funcs[i] = play_blowhole

pick_instrument()
# play_randomized_phrase(selected_instruments[0])
doTogether(instrument_funcs[0], instrument_funcs[1], instrument_funcs[2], play_randomized_beat)
