

#Order the Result

# The json.dumps() method has parameters to order the keys in the result:
#Use the sort_keys parameter
# to specify if the result should be sorted or not:




import  json



x = {
    "name": "john",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "silly"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", ",pg": 24.1}
    ]
}


# sort the results alphabetically bu keys:
print(json.dumps(x, indent=4, sort_keys=True))