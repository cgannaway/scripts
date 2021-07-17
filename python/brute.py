
import time
#import keyboard
start = ""
def alter(sentence,character):
    trial = 0
    if(character != len(sentence)):
        if(sentence[character].isalpha()):
            s = sentence
            s = s[:character] + s[character].upper() + s[character + 1:]
            alter(s,character+1)
        s2 = sentence
        alter(s2,character+1)
    else:
        print("Trial #" + str(trial) +":" + sentence)
        trial += 1
        write(sentence)
        

def pause():
    time.sleep(2)


def write(word):
    pass


pause()
alter(start,0)
