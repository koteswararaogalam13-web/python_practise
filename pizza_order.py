#this program calculates the amount for pizza order
#this file saved as pizza_order.py
size=input("Enter the size of a pizza(small/medium/large):")
bill=0
if size=='small' or size=='SMALL':
    bill+=100
    print("The bill is 100 rupees.")
elif size=='medium' or size=='MEDIUM':
    bill+=200
    print("The bill is 200 rupees.")
else:
    bill+=300
    print("the bill is 300 rupees.")
add_pepperoni=input("do you want pepperoni or not?")
if add_pepperoni=="yes" or add_pepperoni=="YES":
    if size=='small' or size=='SMALL':
        bill+=20
    else:
        bill+=50
extra_cheese=input("Do you want extra cheese not?")
if extra_cheese=="yes" or extra_cheese=="yes":
    bill+=20
print(f"the total bill is {bill}")
