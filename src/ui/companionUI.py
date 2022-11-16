import tkinter
import tkinter.filedialog
from tkinter import ttk
#Needed for normalizing the filepath between different OSes.
import pathlib


class companionUI:
    def __init__(self):
        self.setupUI()
        self.version = "0.0.1"
        self.file2Send = None
        self.file2Recieve = None
    def getVersion(self):
        return self.version
    def setupUI(self):
        print("setting up")
        self.rootUI = tkinter.Tk()
        self.rootUI.minsize(300,500)
        self.rootUI.title("MoneroSigner Companion")
        self.setupMenu()
        self.setupSendFrame()
        self.setupDivider()
        self.setuprecieveFrame()
        self.rootUI.mainloop()
    # Setup menu sets up the file menu dialog
    def setupMenu(self):
        menubar = tkinter.Menu(self.rootUI)
        menubar.config(bg="white")
        self.rootUI.config(menu=menubar)
        fileMenu = tkinter.Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.rootUI.quit())
        menubar.add_cascade(label="File", menu=fileMenu)

        helpMenu = tkinter.Menu(menubar)
        helpMenu.add_command(label="about", command=lambda:print("about application"))
        menubar.add_cascade(label="Help", menu=helpMenu)
    def setupSendFrame(self):
        #The Send Frame is the UI frame holding all the send transaction UI elements
        sendFrame = tkinter.Frame(self.rootUI)
        sendFrame.grid(row=0,column=0,  sticky=tkinter.EW)
        sendFrame.grid_columnconfigure(0,weight=1)
        self.rootUI.grid_columnconfigure(0,weight=1)
        # sendFrame.config(bg="black")
        sendHeader = tkinter.Label(sendFrame, text="Send to Monerosigner", height=1, font=('TkFixedFont', 16))
        sendHeader.grid(row=0, column=0, pady=(5,10),  columnspan=3)
        #setup the file select
        sendFileSelectLabel = tkinter.Label(sendFrame, text="Unsigned Transaction to send:", height=0, font=('TkFixedFont', 10))
        sendFileSelectLabel.grid(row=2, column=0,  columnspan=2)

        sendSelectFile = tkinter.Button(sendFrame, text="selectTx", command=self.selectFile).grid(row=2, column=4)
        sendStartSending = tkinter.Button(sendFrame, text="start", command=self.send2signer).grid(row=3, column=4, sticky=tkinter.EW)
    def setupDivider(self):
        # sets up a divider UI element between the send and recieveFrame
        divider = tkinter.ttk.Separator(self.rootUI, orient=tkinter.HORIZONTAL).grid(row=1,column=0,pady=(5,5), columnspan=12, sticky=tkinter.EW)
    def setuprecieveFrame(self):
        # recieveFrame is the UI frame holding all the recieve UI elements
        recieveFrame = tkinter.Frame(self.rootUI)
        recieveFrame.grid(row=2,column=0,  sticky=tkinter.EW)
        recieveFrame.grid_columnconfigure(0,weight=1)
        recieveHeader = tkinter.Label(recieveFrame, text="Recieve from Monerosigner", height=1, font=('TkFixedFont', 16))
        recieveHeader.grid(row=0, column=0, pady=(5,5), columnspan=3)
        #label for recieve buttons
        recieveFileSelectLabel = tkinter.Label(recieveFrame, text="Where to save Signed TX:", height=0, font=('TkFixedFont', 10))
        recieveFileSelectLabel.grid(row=2, column=0,  columnspan=2)
        #revieve and save
        recieveSelectFile = tkinter.Button(recieveFrame, text="txName", command=self.selectFile).grid(row=2, column=4)

        recieveStartSending = tkinter.Button(recieveFrame, text="start", command=self.grids).grid(row=3, column=4, sticky=tkinter.EW)


    def selectFile(self):
        file = tkinter.filedialog.askopenfile(mode='r')
        if file:
            p = pathlib.Path(file.name)
            print(p)
            self.file2Send = p
            return p
        else:
            return False
    # function to debug number of grids
    def grids(self):
        x = self.rootUI.grid_size()
        print(x)
    def send2signer(self):
        print(self.file2Send)
