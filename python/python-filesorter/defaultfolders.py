import os, sys
import setup

def create():
    #desktop folders
    if not os.path.exists(os.path.join("C:\\", os.environ["HOMEPATH"], "Desktop\SORTER")):
        os.makedirs(os.path.join("C:\\", os.environ["HOMEPATH"], "Desktop\SORTER"))

    #storage folders
    #image
    if not os.path.exists(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Images")):
        os.makedirs(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Images"))
    #video
    if not os.path.exists(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Videos")):
        os.makedirs(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Videos"))
    #doc
    if not os.path.exists(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Documents")):
        os.makedirs(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Documents"))
    #compressed
    if not os.path.exists(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Compressed_files")):
        os.makedirs(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Compressed_files"))
    #music
    if not os.path.exists(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Music")):
        os.makedirs(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Music"))
    #adobe
    if not os.path.exists(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Adobe")):
        os.makedirs(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Adobe"))
    #other
    if not os.path.exists(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Other")):
        os.makedirs(os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Other"))

def writetofile():
    i = os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Images")
    v = os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Videos")
    d = os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Documents")
    c = os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Compressed_files")
    m = os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Music")
    a = os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Adobe")
    o = os.path.join("C:\\", os.environ["HOMEPATH"], "Documents\Sorter\Other")

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
    create()
    writetofile()
    setup.exit()

if __name__ == "__main__":
    main()

