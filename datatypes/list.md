# LIST

## What is list?

* It is the most versatile datatype in python. It includes comma separated values that are enclosed in square brackets. List is a type of mutable sequence in python. 

* Every element in the list is assigned a number i.e. index/position starting from 0.

* We can perform slicing, indexing, adding, multiplying and other functions on list.

* The items in the list need not be of same type.

### Creating an empty list:
	
list_name = []

Example:
Mybooks = []
L1 = []

### Creating a list with items:

Listname = [item1, item2, item3]

Example :
L2 = [1,2,3,4,5]
S = [‘15BIT001’, ‘XYZ’, 99.9] #shows that the items need not be of the same type.
	
### Accessing Values in the list

We can use the index operator [] to access an item in a list. Index starts from 0. So, a list having 5 elements will have index from 0 to 4.

Like L1[3] points to the 4th element from left in L1.

Python also allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.


### Slicing lists in Python

We can access a range of items in a list by using the slicing operator (colon). If we want to access a range, we need two index that will slice that portion from the list.

### How to change or add elements to a list?

* We can use assignment operator (=) to change an item or a range of items.

* We can add one item to a list using append() method or add several items using extend()method.

* We can also use + operator to combine two lists. This is also called concatenation.(here,provided both the elements are lists)

* The * operator repeats a list for the given number of times.

* We can insert one item at a desired location by using the method insert() .

* How to delete or remove elements from a list?

* We can delete one or more items from a list using the keyword del. It can even delete the list entirely.

* We can also delete items in a list by assigning an empty list to a slice of elements.

* We can use remove() method to remove the given item or pop() method to remove an item at the given index.

* The pop() method removes and returns the last item if index is not provided.

## Python List Methods

Methods that are available with list object in Python programming are tabulated below.
They are accessed as list.method(). Some of the methods have already been used above

### Python List Methods

* append() - Add an element to the end of the list

* extend() - Add all elements of a list to the another list

* insert() - Insert an item at the defined index

* remove() - Removes an item from the list

* pop() - Removes and returns an element at the given index

* clear() - Removes all items from the list

* index() - Returns the index of the first matched item

* count() - Returns the count of number of items passed as an argument

* sort() - Sort items in a list in ascending order

* reverse() - Reverse the order of items in the list

* copy() - Returns a shallow copy of the lis


## Built-in Functions with List

Built-in functions are used with list to perform different tasks.

Function|Description
--------|-----------
all()|Return True if all elements of the list are true (or if the list is empty).
any()|Return True if any element of the list is true. If the list is empty, return False.
enumerate()|Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()|Return the length (the number of items) in the list.
list()|Convert an iterable (tuple, string, set, dictionary) to a list.
max()|Return the largest item in the list.
min()|Return the smallest item in the list
sorted()|Return a new sorted list (does not sort the list itself).
sum()|Return the sum of all elements in the list.

## List Comprehension

List comprehension consists of an expression followed by ‘for statement’ inside square brackets.

A list comprehension can optionally contain more ‘for’ or ‘if statements’. An optional ’if statement’ can filter out items for the new list.

The list comprehensions are easy to code and likely to run faster than the conventional methods of creating lists.

You can read more about lists on:
https://www.geeksforgeeks.org/python-list/
https://www.tutorialspoint.com/python/python_lists.htm

