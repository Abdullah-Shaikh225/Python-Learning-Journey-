# WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENT[1,2,3,2,1],[1,"abc","abd",1]
numlist = [1,2,3,2,1]
alphalist = [1,"abc","abc",1]
numlist.copy()
alphalist.copy()
alphacopy = alphalist.copy()
alphacopy.reverse()
numcopy = numlist.copy()
numcopy.reverse()

if(numcopy == numlist):
    print("its palindrome")
else:
    print("its not palindrome")
if(alphacopy == alphalist):
    print("palindrome")
else:
    print("not palindrome")