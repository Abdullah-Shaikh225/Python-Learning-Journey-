# WAP TO ENTER MARKS OF 3 SUBJECTS FROM USER AND STORE THEM IN DICTIONARY. START WITH AN EMPTY DICTINORY
# AND ADD ONE BY ONE. USE SUBJECT NAME AS KEY AND MARKS VALUE.
maths = int(input("enter your marks in maths =:"))
history= int(input("enter your marks in history =:"))
english = int(input("enter your marks in english =:"))
dic = {
    "maths" : maths,
    "history" : history,
    "english" : english
}
print(dic)