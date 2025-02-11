# update Dictionary

# the update() method will update
# the dictionary with the items from a given argument.
# if the item does not exists the item will be added
# the argument must be a dictionary, or an iterable object with key value pairs

# add a color item to the dictionary by using the update() method?

thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}

thisdict.update({"key": "red"})
print(thisdict)