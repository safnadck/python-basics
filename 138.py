#Convert from Python to JSON
#If you have a Python object,

# you can convert it into a JSON string by
# using the json.dumps() method.

#Convert from Python to JSON?

import  json

# a python object (dict):

x = {
    "name": "john",
    "age": 36,
    "city": "New York"
}

# convert into json

y = json.dumps(x)
# the result is a json string

print(y)