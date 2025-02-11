# add a new item to the original dictionary
# and see that the values lists get updated as well:

car = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}

x = car.values()
print(x)  # before the change


car["color"] = "red"
print(x)  # after the change