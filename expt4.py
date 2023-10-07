#Program to demonstrate use of tuples
from pprint import pprint
t =()
l = []

def menu():
    print("\n///MENU///")
    print("1. Create & display tuple")
    print("2. Display details of a student 'Python'")
    print("3. Sort nested tuple")
    print("4. Exit")
    return (int(input("\nEnter your choice: ")))



def read():
    global t
    n = int(input("\nEnter the no. of students: "))
    for i in range(0,n):
        print("\nEnter details for student", i+1, ": ")
        name = input("\nEnter Name: ")
        rno = input("Enter Roll no: ")
        print("Enter the Marks for 5 subjects: ")
        marks = [int(x) for x in input().split()]
        t1 = (rno, name, marks)
        l.append(t1)
        
    t = tuple(l)   
    print("\nDisplaying the student details:-")
    for i in range(0,n):
        print("\nRoll no: ", t[i][0])
        print("Name: ", t[i][1])
        print("Marks: ", t[i][2])
        print("\n------------------------------")
    
    return n

def find(n):
    flag = 0
    for x in t:
        if x[1]=='Python':
            print("\nThe name 'Python' found in tuple")
            print(x)
            flag = 1
            break
            
    if flag==0:
        print("\nThe name 'Python' not found")
        
def sort():
    sortedt = sorted(t, key = lambda x : x[1])
    print("\nThe sorted tuple is:-\n")
    pprint(sortedt)
    
c=0
while(c!=4):
    c=menu()
    if c==1:
        n=read()
    elif c==2:
        find(n)
    elif c==3:
        sort()
    elif c!=4:
        print("\nIncorrect choice")
