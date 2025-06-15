# WAP TO FIND THE FACTORIAL NUMBER OF GIVEN USER INPUT(USING FOR LOOP) 
n = int(input("enter a number"))
factorial = 1
for el in range(1,n+1):
    factorial *=el

print(factorial)