# you can use index numbers {0}

# to be sure the arguments are placed in the correct placeholders:



quantity = 3
itemno = 567
price = 47.95

myorder = "I want to pay {2} dollars for {0} piece of items {1} "

print(myorder.format(quantity, itemno, price))