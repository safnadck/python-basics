# remove list items
from os import remove

# the remove() method removes the specified item

# remove "banana


thislist = ["apple", "banana", "cherry"]

thislist.remove(("banana"))

print(thislist)


#if there are more than one item with the specified value,

# the remove() method removes the first occurance:

# remove the first occurance of "banana"


thislist1 = ["apple", "banana", "cherry", "bananan", "kiwi"]

thislist1.remove("banana")

print(thislist1)