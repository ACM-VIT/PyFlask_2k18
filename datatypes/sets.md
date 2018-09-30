# SETS

**What are sets?**

Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.

**Why use sets?**

Set have unique values. They eliminate duplicates. Python’s set class represents the mathematical notion of a set. The elements in the set are immutable(cannot be modified) but the set as a whole is mutable. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. 

**Python Frozenset**

Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. This datatype supports methods like difference(), intersection(), union(), etc. Being immutable it does not have method that add or remove elements.

## Methods for Sets

**1. add(x) and update(x) Method:** 

We can add single element using the add() method and multiple elements using the update()method. The update() method can take tuples, lists, strings or other sets as its argument.

Eg.people = {"Jay", "Idrish", "Archil"}
people.add("Daxit") 

**2. union(s) Method:**

Returns a union of two set.Using the ‘|’ operator between 2 sets is the same as writing set1.union(set2)
Eg. 
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
population = people.union(vampires)
you could also use
population = people|vampires

**3.intersect(s) Method:** 

Returns an intersection of two sets.The ‘&’ operator can also be used in this case.
victims = people.intersection(vampires)
you could also use
victims=people & vampires

**4. difference(s) Method:** 

Returns a set containing all the elements of invoking set but not of the second set. We can use ‘-‘ operator here.
safe = people.difference(vampires)
you can also use 
safe= people – vampires

**5. clear() Method:** 

Empties the whole set.
victims.clear()

**Sets and frozen sets support the following operators:**

key in s #containment check

key not in s #non-containment check

s1 == s2 #s1 is equivalent to s2

s1 != s2 #s1 is not equivalent to s2

s1 <= s2 #s1is subset of s2 s1 < s2 # s1 is proper subset of s2 s1 >= s2 # s1is superset of s2

s1 > s2 #s1 is proper superset of s2

s1 | s2 #the union of s1 and s2

s1 & s2 #the intersection of s1 and s2

s1 – s2 #the set of elements in s1 but not s2

s1 ˆ s2 #the set of elements in precisely one of s1 or s2

## Website refrences:

https://www.programiz.com/python-programming/set

https://www.geeksforgeeks.org/sets-in-python/

https://www.learnpython.org/en/Sets

## Youtube refrences:

https://www.youtube.com/watch?v=482kbk1x04w

https://www.youtube.com/watch?v=sBvaPopWOmQ

https://www.youtube.com/watch?v=yXIlZGX7Eqk

https://www.youtube.com/watch?v=Nh6n_4RYcUg