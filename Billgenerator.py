# Making a python project for generating a shop bill, which returns total ammount of all produts in bill and save 
import random
namelist = []
pricelist = []
sum = 0
bill_no = random.randint(1000, 9999)
while(True):
    userInput = input("Enter the name and price of the product:\n")
    if (userInput != 'q'):
        name, price= userInput .rsplit(',',1)
        namelist.append(name)
        pricelist.append(int(price))
        sum = sum + int(price)
    else:
        print("\n--------Final Bill--------\n")
        print(f"Bill number:{bill_no}")
        for i in range(len(namelist)):
            print(f"{namelist[i].ljust(15)} ${pricelist[i]}")
        print("------------------------")
        print(f"Toatl Amount: {sum}")
        print("Thank you for using bill generator")
        with open("bill.txt","w") as file:
            file.write("\n--------Final Bill--------\n")
            file.write(f"Bill number:{bill_no}\n")
            for i in range(len(namelist)):
                file.write(f"{namelist[i].ljust(15)} ${pricelist[i]}\n")
            file.write("------------------------\n")
            file.write(f"Toatl Amount: {sum}\n")
            file.write("Thank you for using bill generator\n")

        break