# add a new item to the original dictionary,
# and see that the items lista gets updated as well

car = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}

x = car.items()
print(x)  # before the change


car["color"] = "red"
print(x)  # after the change