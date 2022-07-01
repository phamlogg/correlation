# coding: utf-8

# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
import platform
import sys

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("700x350")

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Excel files', '*.xlsx')])
    if file:
        filepath = os.path.abspath(file.name)
        Label(win, text="The File is located at : " + str(filepath), font=('Aerial 11')).pack()

    if platform.system() == 'Windows':
        os.system(f'python {os.path.abspath("correlation.py")} {filepath}')
    else:
        os.system(f'python3 {os.path.abspath("correlation.py")} {filepath}')

# Add a Label widget
label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button
ttk.Button(win, text="Open Excel File", command=open_file).pack(pady=20)
ttk.Button(win, text="Quit", command=sys.exit).pack(pady=20)

win.mainloop()
