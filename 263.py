# make a change in the original dictiinary
# and see that the value lists get updated as well:

car = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}

x = car.values()
print(x)  # before the change


car["year"] = "2020"
print(x)  # after the change