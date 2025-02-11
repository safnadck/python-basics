# update Dictionary
#the update() method will updatethe dictionary
# with the items from the given argument.

# the argument must be a dicionary,
# or an iterable object with key: value pairs.
# update the "year" of the car by using the update() method:

thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}

thisdict.update({"year": 2020})
print(thisdict)