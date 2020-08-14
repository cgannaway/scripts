import os, glob, sys


def ascii():
    print("\n______ _ _   _       _        _     _     _   \n| ___ (_) | | |     | |      | |   (_)   | |  \n| |_/ /_| |_| | ___ | | ___  | |    _ ___| |_ \n|  __/| |  _  |/ _ \| |/ _ \ | |   | / __| __|\n| |   | | | | | (_) | |  __/ | |___| \__ \ |_ \n\_|   |_\_| |_/\___/|_|\___| \_____/_|___/\__|\n\n _____                           _            \n/  __ \                         | |           \n| /  \/ ___  _ ____   _____ _ __| |_ ___ _ __ \n| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|\n| \__/\ (_) | | | \ V /  __/ |  | ||  __/ |   \n \____/\___/|_| |_|\_/ \___|_|   \__\___|_|   ")


def getFilename():
    txtfiles = []
    for file in glob.glob("*.txt"):
        txtfiles.append(file)

    ascii()
    print("\nText Files Found in Directory:")
    print(txtfiles)
    ans = input("\nwhat is the name of the file? >> ")
    return ans

def createNewFile(filename):
    newname = filename[0:-4] + "_output.txt"
    return open(newname, "w+")

def addZeros(filename):
    fileout = createNewFile(filename)
    with open(filename, 'r') as filedata:
        for line in filedata:
            newline = "0.0.0.0 " + line
            fileout.writelines(newline)

def exitMessage():
    input("\nComplete. (Press enter to continue)")

if __name__ == "__main__":
    addZeros(getFilename())
    exitMessage()
    sys.exit()
    