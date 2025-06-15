# Making a python project for generating a shop bill, which returns total ammount of all produts in bill
namelist = []
pricelist = []
sum = 0
while(True):
    userInput = input("Enter the name and price of the product:\n")
    if (userInput != 'q'):
        name, price= userInput .rsplit(',',1)
        namelist.append(name)
        pricelist.append(int(price))
        sum = sum + int(price)
    else:
        print("products",namelist)
        print("price",pricelist)
        print(f"Your bill total is: {sum}")
        print("Thank You For Using Bill generator")
        break
