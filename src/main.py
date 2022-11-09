# from libs.moneroSignerLib import Companion

from ui.companionUI import companionUI

# import tkinter as tk
# from tkinter import *
import tkinter
import tkinter.filedialog
from tkinter import ttk


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
        print(file)
        return file
    else:
        return False

def grids():
    x = rootUI.grid_size()
    print(x)


UI = companionUI()
print(UI.getVersion())


rootUI = tkinter.Tk()

rootUI.minsize(300,500)
rootUI.title("MoneroSigner Companion")

setupMenu(rootUI)

#The Send Frame
sendFrame = tkinter.Frame(rootUI)
sendFrame.grid(row=0,column=0,  sticky=tkinter.EW)
sendFrame.grid_columnconfigure(0,weight=1)
rootUI.grid_columnconfigure(0,weight=1)

# sendFrame.config(bg="black")
sendHeader = tkinter.Label(sendFrame, text="Send to Monerosigner", height=1, font=('TkFixedFont', 16))
sendHeader.grid(row=0, column=0, pady=(5,5),  columnspan=3)


#setup the file select
sendSelectFile = tkinter.Button(sendFrame, text="selectTx", command=selectFile).grid(row=2, column=4)

sendStartSending = tkinter.Button(sendFrame, text="start", command=grids).grid(row=3, column=4, sticky=tkinter.EW)


#the divider
# deviderFrame = tkinter.Frame(rootUI)
# deviderFrame.grid(row=1,column=0)
divider = tkinter.ttk.Separator(rootUI, orient=tkinter.HORIZONTAL).grid(row=1,column=0,pady=(5,5), columnspan=12, sticky=tkinter.EW)
# divider.pack(fill="x")


#The Recieve Frame
recieveFrame = tkinter.Frame(rootUI)
recieveFrame.grid(row=2,column=0,  sticky=tkinter.EW)
recieveFrame.grid_columnconfigure(0,weight=1)

# recieveFrame.config(bg="red")

recieveHeader = tkinter.Label(recieveFrame, text="Recieve from Monerosigner", height=1, font=('TkFixedFont', 16))
recieveHeader.grid(row=0, column=0, pady=(5,5), columnspan=3)


#revieve and save
recieveSelectFile = tkinter.Button(recieveFrame, text="selectTx", command=selectFile).grid(row=2, column=4)

recieveStartSending = tkinter.Button(recieveFrame, text="start", command=grids).grid(row=3, column=4, sticky=tkinter.EW)



rootUI.mainloop()
