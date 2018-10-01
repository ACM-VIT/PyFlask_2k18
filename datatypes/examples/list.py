#empty list
my_list=[]
#list of integers
integers = [1,2,3]
#list with mixed datatypes
mixed = [1,"Hello",2.0]
#nested list
nested = [1,[1,2,3],3]

print(integers[0]) # prints 1

print(nested[1][1]) #prints  2

print(integers[-1]) #prints 3

my_list = ['h','e','l','l','o']
# elements 3rd to 5th
print(my_list[2:4])

# elements beginning to 3rd
print(my_list[:-2])

# elements 3rd to end
print(my_list[2:])

# elements beginning to end
print(my_list[:])

odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            
# Output: [1, 4, 6, 8]

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  
# Output: [1, 3, 5, 7]

odd.append(9) #adds 9 at the end

odd.extend([11,13]) # output : [1,3,5,7,9,11,13]

print(odd + [15,17]) # we canalso use + to add the lists and it is known as concatenation
# output [1,3,5,7,9,11,13,15,17]

del odd[2] #deletes 5

del odd[1:5] #delets multiple items

del odd # deletes the list

print(odd) #this gives an error

my_list.remove('h') #removes 'h'

my_list.pop(1) #deletes the element at the index 1

my_list.pop() #deletes the element which is in the ending

#defining my_list again
my_list = [3, 8, 1, 6, 0, 8, 4]

# Output: 1
print(my_list.index(8)) #gives the index of the first occurence of 8

# Output: 2
print(my_list.count(8)) #counts the number of times 8 comes in the list

my_list.sort() # sorts the list in ascending order

# Output: [0, 1, 3, 4, 6, 8, 8] 
print(my_list)

my_list.reverse() #reverses the given list

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)

pow2 = [2 ** x for x in range(10)] #list comprehension is used to create a list 

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

new_list = [x+y for x in ['Python ','C '] for y in ['Language','Programming']]

print(new_list)
#output is ['Python Language','Python Programming','C Language','C Programming]