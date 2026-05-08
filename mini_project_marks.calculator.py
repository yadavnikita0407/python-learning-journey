#student_marks_mini_project
marks=[]
for student in range(5):
    m=int(input(f"Enter the marks of subject {student+1} :"))
    marks.append(m)
print("marks are ",marks )
print("Total : ",sum(marks))
print("average :",sum(marks)/5)
ave=sum(marks)/5
if ave<=100 and ave >=90 :
    print("Grade : A")
elif ave<=90 and ave >=80:
    print("Grade : B")
elif ave<=80 and ave >=70:
    print("Grade : C")
else :
    print("Grade : D")
