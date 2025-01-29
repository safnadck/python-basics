# convert a python object containing all the leggal data types ?


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

print(json.dumps(x))