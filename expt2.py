def main():
    print("1. Palindrome\n")
    print("2. Factorial\n")
    print("3. Exit\n")
    return(int(input("Enter your choice: ")))

def palindrome():
    arif = input("Enter the Value: \n")
    rev = arif [: : -1]
    if(arif==rev):
        print(arif,"is palindrome\n")
    else:
        print(arif,"is not a palindrome\n")

def fact():
    number = int(input("Enter the number: \n"))
    factorial = 1
    if(number<0):
        print("Factorial of negative does not exist")
    elif(number>=2):
        for num in range(number,1,-1):
            factorial=factorial*num
        
        print("{}! = {}".format(number,factorial))
    else:
        print("{}! = {}".format(number,factorial))

c = 0
while(c!=3):
    c=main()
    if(c==1):
        palindrome()
    elif(c==2):
        fact()
