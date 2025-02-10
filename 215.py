# remove items

# Note you cannot remove items in a tuple


thistupke = ("apple", "banana", "cherry")
y = list(thistupke)
y.remove("apple")
thistupke = tuple(y)

print(thistupke)