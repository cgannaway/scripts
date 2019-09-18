def main():
   messagein = raw_input("Enter your message: ")
   while True:
      try:
         key = input("enter numerical key value: ")
         break
      except ValueError:
         print "try again"

   cipher(messagein ,key)


def cipher(plaintext,key):
   ciphertext = ''
   for i in range(len(plaintext)):
      position = i*key
      while position > len(plaintext):
         position -= len(plaintext)
      ciphertext = ciphertext + plaintext[position]
         
   print ciphertext


if __name__ == '__main__':
   main()
