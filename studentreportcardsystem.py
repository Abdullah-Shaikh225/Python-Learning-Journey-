# Student report card system
Name = input("Enter your name -:")
RollNumber = int(input("Enter your Roll Number -:"))
English = int(input("Enter your marks in English subject -:"))
Hindi = int(input("Enter your marks in hindi subject -:"))
Maths = int(input("Enter your marks in maths subject -:"))
Science = int(input("Enter your marks in science subject -:"))
History = int(input("Enter your marks in history subject -:"))
# Total marks of student
marks = English + Hindi + Maths + Science + History
print("Marks of student -:", Name)
print(marks)
# percentage of student
Totalmarks = 500
Percentage = (marks/500) * 100
print("Percenatge of student -:", Percentage)
# Garde of student
if(Percentage >=90):
    garde = "A"
elif(Percentage >=80 and Percentage < 90):
    grade = "B"
elif(Percentage >=70 and Percentage < 80):
    grade = "C"
else:
    grade = "D"
    print(grade)
# complete result
print(Name)
print(RollNumber)
print("Total marks obtained -:", marks)
print("Percentage of -:",Name," ",Percentage)
print("Grade obtanied to student -:",grade)
