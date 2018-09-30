### Creating Tuples
```python
college=("VIT","DTU","IIT")
```

### Another method for creating tuples
```python
Laptops=tuple(("Macbook-Air","Macbook-Pro","HP-Pavillion"))
print(Laptops)
#This will print the Laptops tuple
```

### Accessing Tuples
```python
ACM_WEB=("Aditya","Shubham","Rakshit")
print(ACM_WEB[0])
#This will print Aditya
```
### Immutablity of Tuples
**Example1**
```python
ACM_WEB={"Aditya","Shubham","Rakshit"}
ACM_WEB[0]="Shivank"
print(ACM_WEB)
#This will still print the original tuple
```
**Example2**
```python
pokemon=("Pickachu","Charizard","Blastoise")
pokemon[3]="Mr.Mime"
#This will raise an error
print(pokemon)
```
### Looping Through a Tuple
```python
sports=("Cricket","Football","Basketball")
for x in sports:
	print(x)
```
### Calculating Tuple Length
```python
pokemon=("Pickachu","Charizard","Blastoise")
pokemon[3]="Mr.Mime"
#This will raise an error
print(pokemon)
```
### Deleting Tuple
```python
pokemon=("Pickachu","Charizard","Blastoise")
del pokemon
#This will delete the Tuple
```
### count() method of tuples

```python
# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'o', 'e', 'i', 'u')

# count element 'i'
count = vowels.count('i')

```
The ouput will be :3

### index() method of tuples
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




