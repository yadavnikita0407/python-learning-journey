#condition practice
#1)check if number is even or odd
num=int(input("Enter the number "))
if num % 2==0:
    print(num,"is a even number ")
else:
    print(num,"is a odd number ")

#2)check number is positive,negative or zero
num=int(input("Enter the number :"))
if num>0:
    print(num," is a positive number ")
elif num<0:
    print(num," is a negative numbeer ")
else:
    print(" is a zero ")

#3) find the largest of 3 number
n1=int(input("Enter the number 1: "))
n2=int(input("Enter the number 2: "))
n3=int(input("Enter the number 3: "))

if (n1>n2)and (n1>n3):
    print(n1," is the largest number ")
elif n2>n1 and n2>n3 :
    print(n2, " is the largest number ")
else:
    print(n3," is the largest number ")

#4)assign grade based on marks
total =int(input("enter the total marks obtained : "))
no_sub=int(input("enter the total number of subject : "))
avg=total/no_sub
print(avg)
if avg<=100 and avg>=90:
    print(" passed with A+ grade")
elif avg<=80 and avg>=70 :
    print (" passed with B grade ")
elif avg<=60 and avg>=50 :
    print(" passed with C grade")
else:
    print(" fail ")
