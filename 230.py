# add sets

# to add items from another set into the current set,
# use the update() method

thisset = {"apple", "banana", "cherry"}

tropical = {"pinapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)