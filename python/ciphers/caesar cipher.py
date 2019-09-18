
#python 2.7
Alphabet = "abcdefghijklmnopqrstuvwxyz"

#main takes in info and feeds it to cipher
def main():
    
    messagein = raw_input("What do you want to translate? >>> ")

    messagein = messagein.lower()

    mode = ''
    
    while True:
        mode = raw_input("Enter a mode: E(Encrypt) D(decrypt)>>> ")
        mode = mode.upper()
        if mode == 'E' or mode == 'D':
            break

        
    while True:
        try:
            key = raw_input("Enter Numerical Key Value >>> ")
            key = int(key)
            break
        except ValueError:
            print("That's not a integer. try again")



    cipher(messagein, mode, key)
    

#main program
def cipher(messagein, mode, key):
    messageout = ''
    
    #loop
    for i in messagein:
        
        #handles spaces
        if i == ' ':
            messageout = messageout + ' ' 
        #handles special characters
        if i not in Alphabet:
            messageout = messageout + i
        #main cipher
        if i in Alphabet:
            position = Alphabet.find(i)
            #encrypt
            if mode == 'E': 
                position += key
                #handles wraparound
                while position >= 26:
                    position -= 26
            #decrypt
            if mode == 'D': 
                position -= key
                #handles wraparound
                while position <= 0:
                    position += 26
            
            messageout = messageout + Alphabet[position]
    print "message :"
    print messageout

main()
