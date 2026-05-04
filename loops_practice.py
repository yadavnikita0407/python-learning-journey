#1) print numbers 1 to 10
for i in range(11):
    print("its",i)

#2)even numbers from 1 to 10
for i in range(11):
    if i%2==0:
        print("even :",i)
    else:
        print("odd :",i)

#3)total marks using input
total = 0
for i in range(5):
    marks=int(input(f"Enter the marks of subject {i+1}: "))
    total += marks
print("The total of 5 subjects is :",total)

#4)find largest number
largest=-10
for i in range(5):
    num=int(input("Enter the number :"))
    if num>largest:
        print("number is largest ")
    else:
        print("number is not largest ")

#5) expense tracker
total = 0
for i in range(5):
    expence=int(input("Enter your daily expense :"))
    total += expence
print("The total expence is :",total)
