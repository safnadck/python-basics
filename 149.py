#You can control the number of occurrences
# by specifying the maxsplit parameter:


#Split the string only at the first occurrence ?

import  re

txt = "the rain in spain"
x = re.split("\s" , txt, 1)
print(x)