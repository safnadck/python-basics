# add any iterable

# the object in the update() method does not havee to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc..).


thisset = {"apple", "banana", "cherry"}  # set
mylist = ["kiwi", "orange"]  # list


thisset.update(mylist)

print(thisset)