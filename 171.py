#A placeholder can also include a modifier to format the value.

#A modifier is included by adding
# a colon : followed by a legal formatting type,
# like .2f which means fixed point number with 2 decimals:


#Display the price with 2 decimals?

price = 59
txt = f"the price is {price:.2f} dollars"
print(txt)