from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askdirectory
import pygame
import os

# ___________________window________________________________
p = Tk()
p.geometry('800x500')
p.title('shiba player')
# __________________py_game_def_play___________________________
pygame.init()
pygame.mixer.init()
# ____________________open_____________________________________
def open_directory():
    global open_music
    open_dir = askdirectory()
    os.chdir(open_dir)
    music_open = os.listdir(open_dir)
    open_music.delete(0, END)
    for item in music_open:
        if item.endswith((".mp3", ".wav")):
            open_music.insert(END, item)
        else:
            messagebox.showerror('Error', 'Please enter format mp3 or wav')


open_music = Listbox(bg='white', bd=8, relief=GROOVE)
open_music.place(x=0, y=0, width=800, height=298)
# ____________________def_play_________________________________
def play():
    if open_music.curselection():
        selection = open_music.get(open_music.curselection())
        pygame.mixer.music.load(selection)
        pygame.mixer.music.play()

# ____________________def_stop_________________________________
def stop():
    pygame.mixer.music.stop()

# ____________________def_un_pause________________________________
def un_pause():
    pygame.mixer.music.unpause()

# ____________________def_pause___________________________________
def pause():
    pygame.mixer.music.pause()

# ____________________def_volume____________________________________
def set_volume(v):
    volume = float(v) / 100
    pygame.mixer.music.set_volume(volume)


Label_frame = LabelFrame(p, text='', bg='gray', bd=8, relief=GROOVE)
Label_frame.place(x=0, y=350, width=800, height=150)
# __________________button_play________________________________
bt_play = Button(p, text='Play', fg='white', bg='navy blue', font=('Arial', 15), bd=8, relief=GROOVE, command=play)
bt_play.place(x=20, y=400, height=80, width=150)
# __________________button_stop_________________________________
bt_stop = Button(p, text='Stop', fg='white', bg='red', bd=8, font=('Arial', 15), relief=GROOVE, command=stop)
bt_stop.place(x=190, y=400, height=80, width=150)
# _________________button_un_pause__________________________________
bt_pause = Button(p, text='un pause', fg='white', bg='dark green', bd=8, font=('Arial', 15), relief=GROOVE, command=un_pause)
bt_pause.place(x=350, y=400, height=80, width=150)
# _________________button_pause__________________________________
bt_un_pause = Button(p, text='pause', fg='white', bg='dark green', bd=8, font=('Arial', 15), relief=GROOVE, command=pause)
bt_un_pause.place(x=525, y=400, height=80, width=150)
# _________________button_open__________________________________
bt_open = Button(p, text='Open', fg='white', bg='navy blue', bd=8, font=('Arial', 15), relief=GROOVE, command=open_directory)
bt_open.place(x=690, y=400, height=80, width=100)
# __________________volume______________________________________
volume = Scale(p, from_=0, to_=100, resolution=1, orient=HORIZONTAL, bg='gray', bd=5, relief=GROOVE,
               command=set_volume)
volume.place(x=0, y=292, width=800)
# ________________________run_________________________________
p.mainloop()
