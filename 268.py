# check if key exists

# to determine if a  specified key is present in
# a dictionary use the in keyword:

# check if "model" is presented in the dictionary ?

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

if 'model' in thisdict:
    print("yes, 'model' is  one of the keys in the thisdict dictionary")
else:
    print("not in thisdict  ")