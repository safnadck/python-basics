#Python Iterators

#An iterator is an object that contains a countable number of values.

#An iterattor is an object which consist of the methods
# _iter() and __next_().

#Return an iterator from a tuple, and print each value?

mytuple = ("apple", "banana", "cherry")
miit = iter(mytuple)



print(next(miit))
print(next(miit))
print(next(miit))