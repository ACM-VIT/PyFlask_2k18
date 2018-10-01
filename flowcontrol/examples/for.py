import sys
# Some Examples of the for loop in python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
	#The for loop does not require an indexing variable to set beforehand.

 ### Looping Through a String
for x in "banana":
  print(x)
	#Even strings are iterable objects, they contain a sequence of characters

 ### _end_ argument is used
for i in range(4):
 print(i)
for i in range(4):
 print(i, end=" ")
for i in range(4):
    print(i, end=" :-) ")

 ### The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
	#With the break statement we can stop the loop before it has looped through all the items

### The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
	#With the continue statement we can stop the current iteration of the loop, and continue with the next

### The range() Function
for x in range(6):
  print(x)
	#To loop through a set of code a specified number of times, we can use the range() function

###Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
	#The else keyword in a for loop specifies a block of code to be executed when the loop is finished

### Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
	#A nested loop is a loop inside a loop.
