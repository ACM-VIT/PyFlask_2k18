# Creating Tuples

college=("VIT","DTU","IIT")

# Another method for creating tuples

Laptops=tuple(("Macbook-Air","Macbook-Pro","HP-Pavillion"))
print(Laptops)
#This will print the Laptops tuple

# Accessing Tuples
ACM_WEB=("Aditya","Shubham","Rakshit")
print(ACM_WEB[0])
#This will print Aditya

# Immutablity of Tuples
#**Example1**

ACM_WEB=("Aditya","Shubham","Rakshit")
ACM_WEB[0]="Shivank"
print(ACM_WEB)
#This will still print the original tuple

#**Example2**
pokemon=("Pickachu","Charizard","Blastoise")
pokemon[3]="Mr.Mime"
#This will raise an error
print(pokemon)

# Looping Through a Tuple
sports=("Cricket","Football","Basketball")
for x in sports:
	print(x)

# Calculating Tuple Length
pokemon=("Pickachu","Charizard","Blastoise")
pokemon[3]="Mr.Mime"
#This will raise an error
print(pokemon)

# Deleting Tuple
pokemon=("Pickachu","Charizard","Blastoise")
del pokemon
#This will delete the Tuple

# count() method of tuples

# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'o', 'e', 'i', 'u')

# count element 'i'
count = vowels.count('i')
#The ouput will be :3

# index() method of tuples

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
