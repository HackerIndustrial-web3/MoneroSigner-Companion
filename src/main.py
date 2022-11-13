# from libs.moneroSignerLib import Companion

from ui.companionUI import companionUI

# import tkinter as tk
# from tkinter import *
import tkinter
import tkinter.filedialog
from tkinter import ttk


import pathlib






print("Future home of the companion application")

def setupMenu(_master):
    menubar = tkinter.Menu(_master)
    menubar.config(bg="white")
    _master.config(menu=menubar)

    fileMenu = tkinter.Menu(menubar)
    fileMenu.add_command(label="Exit", command=_master.quit())
    menubar.add_cascade(label="File", menu=fileMenu)

    helpMenu = tkinter.Menu(menubar)
    helpMenu.add_command(label="about", command=lambda:print("about application"))
    menubar.add_cascade(label="Help", menu=helpMenu)

def selectFile():
    file = tkinter.filedialog.askopenfile(mode='r')
    if file:
        print(file.name)
        p = pathlib.Path(file.name)
        print(p)
        return p
    else:
        return False

def grids():
    x = rootUI.grid_size()
    print(x)




UI = companionUI()
print(UI.getVersion())



setupMenu(UI.rootUI)



UI.rootUI.mainloop()
