# create three dictionaries?

# then create one dictionary that will contain
# the other three dictionaries?

child1 = {
    "name": "emil",
    "year": 2004
}
child2 = {
    "name" : "Tobiaz",
    "year" : 2007
}
child3 = {
    "name": "linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily)