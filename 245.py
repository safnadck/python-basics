# you can use the & operator
# instead of the intersection() methode.
# and you will get the same result.

# use & to join two sets?

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)


# the & operator only allows you to join sets with sets

# and not with other data tyhpes

# like you can with the intersection() method