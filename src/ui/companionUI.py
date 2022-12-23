import tkinter
import tkinter.filedialog
from tkinter import ttk
#Needed for normalizing the filepath between different OSes.
import pathlib
#imports for
# import bytes
import qrcode
import base64
import json

class qrHelper:
    def __init__(self):
        #Future versions will use variable versions
        self.QRVERSION = 7
        self.METADATA_SIZE = 37
        #the lenght limits of QR codes
        #In the future will be used for variable lenght
        self.QRLIMITS  = {}
        self.QRLIMITS["2"] = 32 #version 2 25x25
        self.QRLIMITS["3"] = 53 #version 3 29x 29
        self.QRLIMITS["4"] = 78 #version 4 3x33
        self.QRLIMITS["5"] = 106 #v5 37x37
        self.QRLIMITS["6"] = 230 #v6 53x53
        self.QRLIMITS["7"] = 2953 #v7  177x177


    def calcNumFrames(self, _dataSize, _frameSize):
        return (_dataSize // _frameSize) + (1 if (( _dataSize % _frameSize) > 0)  else 0)
    def calcSize(self, _input):
        size = len(_input)
        return size
    def createFrame(_data, _frameSize):
        fullData = memoryview(_data).cast('c')
        # sizeIN = len(_data)
        sizeIN = len(fullData)
        print(f"size of tx {sizeIN}")
        framesNeeded = calcNumFrames(sizeIN, _frameSize)
        print(f"frames needed {framesNeeded}")
        print(f"limit needed {_frameSize}")

        for x in range(0,framesNeeded):
            start = x * _frameSize
            stop = start + _frameSize
            dataSlice = bytes(fullData[start:stop])
            dataSlice = base64.b64encode(dataSlice).decode('ascii')
            print(f"On slice {x} size of data {len(dataSlice)}")
            frame = {
            "index" : x,
            "total" : framesNeeded,
            "data" :  dataSlice
            }
            print(json.dumps(frame))
            qr = qrcode.QRCode(
                version=7,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            img = qrcode.make(frame)
            # img.save(f"outputImg/{x}.png")
            return img


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
