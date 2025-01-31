#Python RegEx

#A RegEx, or Regular Expression,
# is a sequence of characters that forms a search pattern.

#RegEx can be used to check if a string contains
# the specified search pattern.

#RegEx Module
#Python has a built-in package called re,
# which can be used to work with Regular Expressions.


#Import the re module:


#Search the string to see if it starts with
# "The" and ends with "Spain" ?
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("YES! we have a match!")
else:
    print("NO match")




#  ^ -----	Starts with
#  .  ------	Any character (except newline character)
#  *  -------	Zero or more occurrences
#  $ ------	Ends with