import os, sys, shutil, re, time

on = False

def main(): #takes sre patterns and returns them to the loop
    global on
    on = True
    images, videos, docs, compressed, music, adobe = compileext()
    imgpath, vidpath, docpath, comppath, musicpath, adobepath, otherpath = getfilepath()
    sortloop(images, videos, docs, compressed, music, adobe, imgpath, vidpath, docpath, comppath, musicpath, adobepath, otherpath)
    #sortermenu.main()

def sortloop(images, videos, docs, compressed, music, adobe, imgpath, vidpath, docpath, comppath, musicpath, adobepath, otherpath): #runs the sorter
    while True:
        move(images, videos, docs, compressed, music, adobe, imgpath, vidpath, docpath, comppath, musicpath, adobepath, otherpath )
        time.sleep(10)#sleeps 10 minutes before running the loop again

#compiles + sorts extension groups to test files against
def compileext():
    """compiles + sorts extension groups to test files against"""

    images = re.compile(".jpeg|.jpg|.tiff|.gif|.png|.svg|.bmp")
    videos = re.compile(".mp4|.mov|.avi")
    docs = re.compile(".txt|.pdf|.pages|.docx|.doc|.xps|.rtf|.wpd|.xls|.xlsx|.ppt|.pptx")
    compressed = re.compile(".zip|.tar|.iso")
    music = re.compile(".m4a|.m4p|.aac|.mp3|.raw|.wav|.ogg")
    adobe = re.compile(".psd|.aep|.prproj|.ai")

    return images, videos, docs, compressed, music, adobe 

def getfilepath():
    """Gets locations of folders"""
    f = open("locations.txt", "r")
    imgpath = f.readline()
    vidpath = f.readline()
    docpath = f.readline()
    comppath = f.readline()
    musicpath = f.readline()
    adobepath = f.readline()
    otherpath = f.readline()
    
    imgpath = imgpath[0:-1]
    vidpath = vidpath[0:-1]
    docpath = docpath[0:-1]
    comppath = comppath[0:-1]
    musicpath = musicpath[0:-1]
    adobepath = adobepath[0:-1]
    otherpath = otherpath[0:-1]

    f.close()

    return imgpath, vidpath, docpath, comppath, musicpath, adobepath, otherpath


def move(images, videos, docs, compressed, music, adobe, imgpath, vidpath, docpath, comppath, musicpath, adobepath, otherpath):
    """takes files and moves them to a new location"""

    #files = [x for x in os.listdir(os.path.join(os.environ["HOMEPATH"], "Desktop\SORTER"))]
    files = os.listdir(os.path.join(os.environ["HOMEPATH"], "desktop\SORTER\\"))

    
    for x in (files):
        if images.search(x):
            shutil.move(os.path.join(os.environ["HOMEPATH"], "Desktop\SORTER\\", x), os.path.join(imgpath, x))
        elif videos.search(x):
            shutil.move(os.path.join(os.environ["HOMEPATH"], "Desktop\SORTER\\", x), os.path.join(vidpath, x))
        elif docs.search(x):
            shutil.move(os.path.join(os.environ["HOMEPATH"], "Desktop\SORTER\\", x), os.path.join(docpath, x))
        elif compressed.search(x):
            shutil.move(os.path.join(os.environ["HOMEPATH"], "Desktop\SORTER\\", x), os.path.join(comppath, x))
        elif music.search(x):
            shutil.move(os.path.join(os.environ["HOMEPATH"], "Desktop\SORTER\\", x), os.path.join(musicpath, x))
        elif adobe.search(x):
            shutil.move(os.path.join(os.environ["HOMEPATH"], "Desktop\SORTER\\", x), os.path.join(adobepath, x))
        else :
            shutil.move(os.path.join(os.environ["HOMEPATH"], "Desktop\SORTER\\", x), os.path.join(otherpath, x))
        
    z = str(len(files))
    print(z + " Files Moved")
def exit():
    global on
    on = False

def start():
    main()

if __name__ == "__main__":
    start()