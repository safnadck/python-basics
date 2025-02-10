# difference

# the difference() methode will return a neew set
# that will contain only the items from the first set
#that are not presented in the other set.

# keep all items from set1 that are not in set2 ?

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)