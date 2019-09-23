import Tkinter, tkFileDialog
import setup
import os, sys

def takeinput():
    images = tkFileDialog.askdirectory(title="Where would you like the Images Folder to be?")
    videos = tkFileDialog.askdirectory(title="Where would you like the Videos Folder to be?")
    documents = tkFileDialog.askdirectory(title="Where would you like the Documents Folder to be?")
    compressed = tkFileDialog.askdirectory(title="Where would you like the Compressed Files Folder to be?")
    music = tkFileDialog.askdirectory(title="Where would you like the Music Folder to be?")
    adobe = tkFileDialog.askdirectory(title="Where would you like the Adobe Projects Folder to be?")
    other = tkFileDialog.askdirectory(title="Where would you like the Other Folder to be?")

    return images, videos, documents, compressed, music, adobe, other

def makefiles(images, videos, documents, compressed, music, adobe, other):
    #desktop folders
    if not os.path.exists(os.path.join("C:/", os.environ["HOMEPATH"], "Desktop/SORTER")):
        os.makedirs(os.path.join("C:/", os.environ["HOMEPATH"], "Desktop/SORTER"))

    #storage folders
    #image
    if not os.path.exists(os.path.join(images, "Images/")):
        os.makedirs(os.path.join(images, "Images/"))
    #video
    if not os.path.exists(os.path.join(videos, "Videos/")):
        os.makedirs(os.path.join(videos, "Videos/"))
    #doc
    if not os.path.exists(os.path.join(documents, "Documents/")):
        os.makedirs(os.path.join(documents, "Documents/"))
    #compressed
    if not os.path.exists(os.path.join(compressed, "Compressed_Files/")):
        os.makedirs(os.path.join(compressed, "Compressed_Files/"))
    #music
    if not os.path.exists(os.path.join(music, "Music/")):
        os.makedirs(os.path.join(music, "Music/"))
    #adobe
    if not os.path.exists(os.path.join(adobe, "Adobe/")):
        os.makedirs(os.path.join(adobe, "Adobe/"))
    #other
    if not os.path.exists(os.path.join(other, "Other/")):
        os.makedirs(os.path.join(other, "Other/"))

def writetofile(images, videos, documents, compressed, music, adobe, other):
    i = os.path.join(images, "Images/")
    v = os.path.join(videos, "Videos/")
    d = os.path.join(documents, "Documents/")
    c = os.path.join(compressed, "Compressed_Files/")
    m = os.path.join(music, "Music/")
    a = os.path.join(adobe, "Adobe/")
    o = os.path.join(other, "Other/")

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
    images, videos, documents, compressed, music, adobe, other = takeinput()
    makefiles(images, videos, documents, compressed, music, adobe, other)
    writetofile(images, videos, documents, compressed, music, adobe, other)
    setup.exit()

if __name__ == "__main__":
    main()