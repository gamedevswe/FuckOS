from tkinter import *
from tkinter import filedialog
import os

def OpenFile():
    filepath = filedialog.askopenfilename(initialdir='/', title='Open Files', filetypes=(("All Files", "*.*"), ("Text Files", '*.txt')))
    os.startfile(filepath)

window = Tk()
button = Button(text='Open', command=OpenFile)
button.pack()
window.mainloop()