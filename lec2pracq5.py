# WAP TO FIND THE GREATEST OF 3 NUMBERS
number1 = int(input("Enter 1st number"))
number2 = int(input("Enter 2nd number"))
number3 = int(input("Enter 3rd number"))

if(number1 > number2 and number1 > number3 ):
    greast = number1
elif(number2 > number1 and number2 >number3):
    greast = number2

elif(number3 > number1 and number3 > number2):
    greast = number3
else:
    print("number are equal")
    greast = number1

print(greast)    