# Add a new item to a the original dictionary
# and see that the keys lists get updated as well ?

car = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}

x = car.keys()
print(x)  # before the change


car["color"] = "white"
print(x)  # after the change