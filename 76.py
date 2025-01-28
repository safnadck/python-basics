# return "orange" instead of  "banana"

fruits = ["apple", "banana", "cherry", "kiwi" ,"mango", "banana"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)