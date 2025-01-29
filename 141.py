#You can also define the separators,

# default value is (", "     ": "),

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

# use . and a space to separate objects,
# and a space,  a =  and a space to separate keys for their values


print(json.dumps(x, indent=4, separators=(". ", " = ")))