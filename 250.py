# the differce_update method will also keep the items

# from the first set that are not in the other set,

# but it will change the original set instead of returning a new set

# use the difference_update() method to keep the items
# that are not presented in both sets ?

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)