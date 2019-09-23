#python 2.7
#counts words and word occurences

from collections import Counter
import os
import re
import csv
import msvcrt as m
import time

#file reading
def read():
    print "Document must be in the same folder as this program"
    while True:
        try:
            document = raw_input("Enter File Name >> ")
            f = open(document, "r")
            break
        except IOError:
            print "File Failed to Open, Try Again"
    data = f.read()
    data = data.lower()
    
    print data####################################
    return data

#starting point
def main():
    words = read()
    count, occurence_wordonly, occurence_numonly = data(words)
    write(count, occurence_wordonly, occurence_numonly)
    stopper()
    
def data(words):
    #split words into a list of words
    listofwords = list(re.split(' ', words))

    print listofwords
    
    newlist = list()
    for i in range(len(listofwords)):
        newlist.append(listofwords[i].replace("\n", ''))
        del listofwords[:1]

    print newlist


    #total wordcount
    count = len(newlist)
    #makes list of ("word", "#of occurences")
    occurence_words = Counter(newlist).most_common()
    
    occurence_num = list()
    occurence_wordonly = list()
    occurence_numonly = list()

    #pulls the numbers out of the first list and puts them in their own list
    for i in range(len(occurence_words)):
        occurence_num.append(re.findall('\d', str(occurence_words[i])))

    #gets rid of formatting in the list ex: (" and ")
    for i in range(len(occurence_words)):
        x = str(occurence_words[i])
        x = x[2:-5]
        occurence_wordonly.append(x)

    #gets rid of formatting in the list ex: (" and ")
    for i in range(len(occurence_num)):
        x = str(occurence_num[i])
        x = x[2:-2]
        occurence_numonly.append(x)
    print occurence_wordonly#########################################
    print occurence_numonly###############################################
    return count, occurence_wordonly, occurence_numonly

#opens csv file
def write(count, occurence_wordonly, occurence_numonly):                         
    with open("output.csv", "w+") as output:
        writer = csv.writer(output, lineterminator='\n')
        #wordformat = workbook.add_format(properties={'font_color': red})

#writes header
        header = ["Word", "Occurences", "Count = " + str(count)]
        writer.writerow(header)

#writes 2 columns
        for i in range(len(occurence_wordonly)):
        
            writer.writerow([occurence_wordonly[i], occurence_numonly[i]])

#stops or restarts program
def stopper():
    print '----------------------------------------------------------'
    print "Successfully outputted to CSV"
    print "Press enter to continue..."
    raw_input()
    print '----------------------------------------------------------'
    print "Would you like to count another file?"
    print "Press enter to continue, otherwise type 'stop'"
    x = raw_input()
    if x == '':
        print '----------------------------------------------------------'
        main()
    else:
        quit()

#runs main() when program starts    
if __name__ == "__main__":
    main()


