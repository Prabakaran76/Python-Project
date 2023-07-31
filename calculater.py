#Calculater
"""num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
sig = input("Enter the sign i.e +, -, *, /, //, % : ")
print("Enter X or x for Exit.")"""

while(True):
    num1 = input("Enter the number1: ")
    if (num1 == "X" or num1 == "x"):
        break
    num2 = int(input("Enter the number2: "))
    sig = input("Enter the sign i.e +, -, *, /, //, % : ")
    print("Enter X or x for Exit.")
    if(sig == "+"):
        print("The Sum of {} + {} is:{} ".format(num1,num2,int(num1)+num2))
    if(sig == "-"):
        print("The Subraction of {} - {} is:{} ".format(num1,num2,int(num1)-num2))
    if(sig == "*"):
        print("The Multipel of {} * {} is:{} ".format(num1,num2,int(num1)*num2))
    if(sig== "/"):
        print("The Division of {} / {} is:{} ".format(num1,num2,int(num1)/num2))
    if(sig== "//"):
        print("The Floor Division of {} // {} is:{} ".format(num1,num2,int(num1)//num2))
    if(sig== "%"):
        print("The Modulo of {} % {} is:{} ".format(num1,num2,int(num1)%num2))
