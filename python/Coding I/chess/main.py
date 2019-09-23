import os

def main():
  filein()
  
def filein():
  document = open('document.txt', 'r')
  lines = document.readlines()
  for j in range(len(lines)):
    if '\n' in lines[j]:
      lines[j] = lines[j][:-1] 

  T = int(lines[0])
  del lines[0]
  pass_data(T, lines)

def pass_data(T, lines): 
  for i in range(T):
    data_ = lines[:3]
    
    data = []

    for i in range(len(data_)):
      data += data_[i].split(',')
    del lines[:3]
    R, C = int(data[0]), int(data[1])
    r1, c1 = int(data[2]), int(data[3])
    r2, c2 = int(data[4]), int(data[5])
    possibilities(R,C,r1,c1,r2,c2)

def possibilities(R,C,r1,c1,r2,c2):
    var = 0
    if R < r1:
        print ("No [out of bounds]")
        var = 1


    if R < r2:
        if var != 1:
            print ("No [out of bounds]")
            var = 1

    if C < c1:
        if var != 1:
            print ("No [out of bounds]")
            var = 1

    if C < c2:
        if var != 1:
            print ("No [out of bounds]")
            var = 1

    if var != 1:
        if r1 % 2 == 0:
            r1 = "even"
        else:
            r1 = "odd"

        if c1 % 2 == 0:
            c1 = "even"
        else:
            c1 = "odd"
        if r2 % 2 == 0:
            r2 = "even"
        else:
            r2 = "odd"
        if c2 % 2 == 0:
            c2 = "even"
        else:
            c2 = "odd"
        if r1 != c1:
            set1 = "diffrent"
        else:
            set1 = "same"

        if r2 != c2:
            set2 = "diffrent"
        else:
            set2 = "same"

        if set1 == set2:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
  main()