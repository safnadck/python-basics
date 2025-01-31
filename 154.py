# print the string pass to the function


import re
txt = "the rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)