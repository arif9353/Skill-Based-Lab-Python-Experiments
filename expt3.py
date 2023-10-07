#program to demonstrate use of lists

arif1=[]
arif2=[]
arif3=[]
arif4=[]
def menu():
    print("1. Even & Odd")
    print("2. Merge & Sort")
    print("3. Minimum & Max")
    print("4. Update & Delete")
    print("5. Adding Names into the list")
    print("6. Exit")
    return (int(input("Enter your choice from above: \t")))

def eveodd():
    for i in arif1:
        if i%2==0:
            arif4.append(i)
        else:
            arif2.append(i)
    print("Even Numbers are:")
    print(arif4)
    print("Odd Numbers are:")
    print(arif2)

def merge():
    arif3 = arif4 + arif2
    print("The merged list is:",arif3)
    arif3.sort()
    print("Sorted list in ascending order is:",arif3)
    print("Sorted list in Descending order is:",arif3[::-1])

def update():
    x = int(input("Enter the element to be placed:"))
    y = int(input("Enter the position for the element to be inserted in the list:"))
    arif1[y]=x
    print("The updated list is:",arif1)
    b = len(arif1)
    arif1.pop(b//2)
    print("After deleting middle element the list is:",arif1)

def minimax():
    print("The minimum element of list is:",min(arif1))
    print("The maximum element of list is:",max(arif1))

def add():
    n1 = int(input("Enter the number of strings to store in list:\t"))
    print("Enter the strings:\t")
    for i in range(0,n1):
        s = input()
        arif1.append(s)
    print("The updated list is:",arif1)
    if 'python' in arif1:
        print("The string 'python' is present in the list")
    else:
        print("The string 'python' is not present in the list")

n = int(input("Enter the number of elements to store in list:\t"))
print("Enter the numbers in List:\t")
arif1 = [int(x) for x in input().split()]
print("The list is:\t", arif1)

c=0
while(c!=6):
    c = menu()
    if c==1:
        eveodd()
    elif c==2:
        merge()
    elif c==3:
        minimax()
    elif c==4:
        update()
    elif c==5:
        add()
    elif c!=6:
        print("Enter a correct choice:")
