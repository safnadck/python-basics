# the format() methods takes unlimited number of arguments

# and are placed into the respective placeholder:


quantity = 3
itemno = 567
price = 47.95

myorder = "I want {} pieces of items {} for {} dollars"

print(myorder.format(quantity, itemno, price))