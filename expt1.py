#PROGRAM FOR SWAPPING TWO NUMBERS AND CHECKING IT'S SIGN

a = input("\nEnter the first number: ")
b = input("\nEnter the second number: ")

print("\nBefore swapping of the two numbers:-")
print('a = ',int(a),'\nb = ',int(b))

temp = int(a)
a = int(b)
b = int(temp)

print("\nAfter swapping the two numbers:-")
print('a = ',int(a),'\nb = ',int(b))

if(int(a)>0):
    print('\nThe number ',a,' is positive')
elif(int(a)==0):
    print('\nThe number ',a,' is zero')
else:
    print('\nThe number ',a,' is negative')