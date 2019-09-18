from Tkinter import *
import defaultfolders, installfolder, individualinstall, sortermenu
import sys

class Window(Frame): #intialize frame

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def init_window(self): #initialize window
        self.master.title("Service Setup") #window title
        self.desc = Label(self.master, text="Choose Where to Install", font=("Helventica", 20))
        self.info = Label(self.master, wraplength=300, text="You can choose where you would like to install the directories. 'Default' will install the directories to 'C:/User/Documents/Sorter/'. 'Install Folder' will let you choose a location to install the required folders to. 'Individual Install' will let you choose the location of each individual folder.")#window label
        
        self.pack(fill=BOTH, expand=1)

        #create buttons
        self.defaultbutton = Button(self.master, text="Default Install", fg="green", command=self.default)
        self.folderbutton = Button(self.master, text="Install Folder", fg="red", command=self.folder)
        self.individualbutton = Button(self.master, text="Individual Install", fg="red", command=self.individual)

        
        #pack buttons/description
        self.desc.pack(expand=True)
        self.info.pack(expand=True)
        self.individualbutton.pack(side=BOTTOM, expand=True)
        self.folderbutton.pack(side=BOTTOM, expand=True)
        self.defaultbutton.pack(side=BOTTOM, expand=True)

    def default(self):
        defaultfolders.main()
    
    def folder(self):
        installfolder.main()
        
    def individual(self):
        individualinstall.main()

if __name__ == "__main__":
    root = Tk()
    root.geometry("500x350")
    root.iconbitmap('favicon.ico')
    installer = Window(root)
    root.mainloop()

def exit():
    sys.exit()
    