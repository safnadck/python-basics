# Loop through Nested Dictionaries

# you can loop through a dictionary
# by using the items() method like this.

# loop through the keys and values of all nested dictionaries?

myfamily = {
    "child1": {
        "name": "email",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3" : {
        "name": "linus",
        "year": 2011
    }
}

for x, z in myfamily.items():
    print(x)

    for y in z:
        print(y + ':', z[y])