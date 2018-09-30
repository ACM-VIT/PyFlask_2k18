#Examples for dictionary

#DEFINING DICTIONARY
#by-default
d = {
	'City': 'Vellore',
	'State': 'Tamil Nadu',
	'Country': 'India',
	'Continent': 'Asia'
}

#defining as a list of tuples
d = dict([
	('City', 'Vellore'),
	('State', 'Tamil Nadu'),
	('Country', 'India'),
	('Continent', 'Asia')
])

#as keyword arguments
d = dict(
	City = 'Vellore',
	State = 'Tamil Nadu',
	Country = 'India',
	Continent = 'Asia'
	)
##ACCESSING VALUES
d['City'] #gives you 'Vellore'

#updating
d['City'] = 'Chennai' #changes the value of key 'City' to 'Chennai'

d['Gallaxy'] = 'Milky-Way Gallaxy' #adds a new key-value pair

#deleting
del d['Country'] #deletes the instance of key-value pair from d of key 'Chennai'

d.pop('Country') #also returns the value of deleted key-value pair

d.popitem() #removes the last item in the dictionary d
##USEFUL FUNCTIONS
#clear
d.clear() #empties the dictionary

#update
d.update({'Planet':'Earth'})
'''This command adds an extra key-value pair to the dictionary
It is analogous to "append" function for list.
We can add any number of key-value pairs using update'''

d.keys()
d.values()
'''to get keys and values
Gives a list of keys and values in a dictionary'''

d.items() #to get both keys and values
