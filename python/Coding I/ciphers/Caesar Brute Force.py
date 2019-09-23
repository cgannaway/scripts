#python 2.7
Alphabet = "abcdefghijklmnopqrstuvwxyz"

def main():
    messagein = raw_input("Enter Text for Brute Force >>> ")
    
    messagein = messagein.lower()
    
    
    cipherbreak(messagein)


def cipherbreak(messagein):
    for key in range(26):
        messageout = ''

        #loop
        for i in messagein:
            
            #main cipher
            if i in Alphabet:
                position = Alphabet.find(i)
                position = position - key
                if position < 0:
                    position = position + 26
            
                messageout = messageout + Alphabet[position]

            else:
                messageout = messageout + i
           
        print("Key: %s; Message: %s" %(key, messageout))
main()
