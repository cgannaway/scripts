import os, sys
import Tkinter, tkFileDialog
import setup

root = Tkinter.Tk()
root.withdraw()

def getlocation():
    location = tkFileDialog.askdirectory(title="Choose where you want to install the folders")
    return location

def createdirs(location):
    #desktop folders
    if not os.path.exists(os.path.join("C:/", os.environ["HOMEPATH"], "Desktop/SORTER")):
        os.makedirs(os.path.join("C:/", os.environ["HOMEPATH"], "Desktop/SORTER"))

    #storage folders
    #image
    if not os.path.exists(os.path.join(location, "Sorter/Images")):
        os.makedirs(os.path.join(location, "Sorter/Images"))
    #video
    if not os.path.exists(os.path.join(location, "Sorter/Videos")):
        os.makedirs(os.path.join(location, "Sorter/Videos"))
    #doc
    if not os.path.exists(os.path.join(location, "Sorter/Documents")):
        os.makedirs(os.path.join(location, "Sorter/Documents"))
    #compressed
    if not os.path.exists(os.path.join(location, "Sorter/Compressed_files")):
        os.makedirs(os.path.join(location, "Sorter/Compressed_files"))
    #music
    if not os.path.exists(os.path.join(location, "Sorter/Music")):
        os.makedirs(os.path.join(location, "Sorter/Music"))
    #adobe
    if not os.path.exists(os.path.join(location, "Sorter/Adobe")):
        os.makedirs(os.path.join(location, "Sorter/Adobe"))
    #other
    if not os.path.exists(os.path.join(location, "Sorter/Other")):
        os.makedirs(os.path.join(location, "Sorter/Other"))

def writetofile(location):
    i = os.path.join(location, "Sorter/Images")
    v = os.path.join(location, "Sorter/Videos")
    d = os.path.join(location, "Sorter/Documents")
    c = os.path.join(location, "Sorter/Compressed_files")
    m = os.path.join(location, "Sorter/Music")
    a = os.path.join(location, "Sorter/Adobe")
    o = os.path.join(location, "Sorter/Other")

    f = open("locations.txt", "w+")

    f.write(i)
    f.write("\n")
    f.write(v)
    f.write("\n")
    f.write(d)
    f.write("\n")
    f.write(c)
    f.write("\n")
    f.write(m)
    f.write("\n")
    f.write(a)
    f.write("\n")
    f.write(o)

    f.close()


def main():
    installfile = getlocation()
    createdirs(installfile)
    writetofile(installfile)
    setup.exit()

if __name__ == "__main__":
    main()