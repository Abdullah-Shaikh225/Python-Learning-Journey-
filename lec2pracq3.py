## WAO TO IMPLEMENT CONDITIONAL STATMENT FOR
# MARKS >= 90, GRADE "A"
# 90> MARKS >= 80, GARDE "B"
# 80 > MARKS >= 70, GRADE "C"
# 70 > MARKS, GRADE "D"
student = int(input("Enter your marks "))
if(student>=90):
    grade = "A"
elif(student >= 80 and student < 90):
    grade = "B"
elif(student >= 70 and student < 80):
    grade = "C"
else:
    grade = "D"

print(grade)    



