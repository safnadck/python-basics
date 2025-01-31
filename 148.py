#The split() Function

#The split() function
# returns a list where the string has been split at each match:

#Split at each white-space character ?

import  re
txt = "the rain in spain"
x = re.split("\s", txt)
print(x)