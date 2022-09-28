from tkinter import *
from tkinter import ttk

root = Tk()
import math
Label(root, text="Year 11 SDD").pack(side=LEFT, padx=10, pady=20)
e = StringVar()
Entry (root, width=40, textvariable=e).pack(side=LEFT)
e.set("'Wow! This is my first GUI'")
