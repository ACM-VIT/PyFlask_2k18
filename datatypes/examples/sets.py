# initialize my_set
my_set = {1,3}
print(my_set)
 # add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)
 # add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)
 # discard an element
# Output: {1, 2, 3}
my_set.discard(4)
print(my_set)
 # clear my_set
#Output: set()
my_set.clear()
print(my_set)
 # initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
 # union of sets
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
A.union(B)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
 # intersection of sets
# Output: {4, 5}
print(A & B)
A.intersection(B)
#Output: {4, 5}
 # difference of sets
# Output: {1, 2, 3}
print(A - B)
A.difference(B)
# Output: {1, 2, 3}
 # initialize A and B frozen sets
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
 # operations on frozen sets
A.isdisjoint(B)
# Output: False
A.difference(B)
# Output: frozenset({1, 2})
A | B
# Output: frozenset({1, 2, 3, 4, 5, 6})
A.add(3)
# Output: will show error "AttributeError: 'frozenset' object has no attribute 'add'"
