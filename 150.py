#The sub() Function

#The sub() function replaces the matches with the text of your choice:

#Replace every white-space character with the number 9 ?


import re

txt = "the rain in spain"
x = re.sub("\s", "9", txt)
print(x)