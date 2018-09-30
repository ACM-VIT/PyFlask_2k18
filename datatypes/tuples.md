# TUPLES

## Definition And Creating Tuples

A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

For example:-
```python
college=("VIT","DTU","IIT")
```
### Another method for creating tuples:-
```python
Laptops=tuple(("Macbook-Air","Macbook-Pro","HP-Pavillion"))
print(Laptops)
#This will print the Laptops tuple
```
## Accessing Tuples

Accessing tuples is quite easy .We just need to make use of the index number of the item

For example:-
```python
ACM_WEB=("Aditya","Shubham","Rakshit")
print(ACM_WEB[0])
#This will print Aditya
```

#### NOTE:- Tuples are immutable.Once you create a tuple, you can't change it.

For example:-
```python
ACM_WEB=("Aditya","Shubham","Rakshit")
ACM_WEB[0]="Shivank"
print(ACM_WEB)
#This will still print the original tuple
```
#### The value will remain the same

## Looping Through a Tuple

A simple way to loop through a tuple is using a for loop

For example:-
```python
sports=("Cricket","Football","Basketball")
for x in sports:
	print(x)
```
## Adding Items to Tuples

It is really important to know that  we cannot add items to a tuple once we create it

For Example:-
```python
pokemon=("Pickachu","Charizard","Blastoise")
pokemon[3]="Mr.Mime"
#This will raise an error
print(pokemon)
```
## Calculating Tuple Length

We make use of the len() method

For Example:-
 ```python
 pokemon=("Pickachu","Charizard","Blastoise")
 print(len(pokemon))
 #It will print 3
 ```
## Removing Items from a Tuple

You cannot remove items from a tuple but you can delete the tuple itself.

For Example:-
```python
pokemon=("Pickachu","Charizard","Blastoise")
del pokemon
#This will delete the tuple
```
## Tuple Methods

Python has a few builtin methods for tuples such as
**count()**
It basically returns count of an item in a tuple
for example:-
```python
# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'o', 'e', 'i', 'u')

# count element 'i'
count = vowels.count('i')

```
**index()**
Searches the tuple for a specified value and returns the position of where it was found
```python
# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')

# element 'e' is searched
index = vowels.index('e')

# index is printed
print('The index of e:', index)

# element 'i' is searched
index = vowels.index('i')

# only the first index of the element is printed
print('The index of i:', index)
```
*The output for this piece of code will be*:-

The index of e: 1
The index of i: 2

For Further references :-
<a>https://www.youtube.com/watch?v=NI26dqhs2Rk</a>
