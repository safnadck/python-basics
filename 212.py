# update Tuple

# Change tuple values
#once a tuple is created , you cannot change its values.

# tuples are unchangeable , or immutable as it also is called.


# you can convert the tuple into a list,
#change the list , and convert the list back into a tuple

# convert the tuple into a list to be able to chnage it


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x  = tuple(y)

print(x)