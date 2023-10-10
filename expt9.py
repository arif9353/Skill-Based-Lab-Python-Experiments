#Program to demonstrate use of python in files.
import os

def menu():
    print("\n///MENU///")
    print("1. To count number of lines, words and characters in a file")
    print("2. To display files in current directory")
    print("3. Exit")
    return(int(input("\nEnter your choice: ")))

c=0

while c!=3:
    c = menu()

    if c==1:

        c=l=w=0
        fname = input("Enter the file name: ")
        f = open(fname+".txt", "r")
        for x in f:
            words = x.split()
            l+=1
            w+=len(words)
            c+=len(x)
        print("No. of lines = ", l)
        print("No. of words = ", w)
        print("No. of characters = ", c)
        f.close()

    elif c==2:

        for subdir, dirs, files in os.walk('./'):
           for file in files:
             print (file)


    elif c!=3:

        print("Incorrect choice")
