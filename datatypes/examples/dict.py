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

#deleting
del d['Country'] #deletes the instance of key-value pair from d of key 'Chennai'

##USEFUL FUNCTIONS
#update
d.update({'Planet':'Earth'})
'''This command adds an extra key-value pair to the dictionary
It is analogous to "append" function for list'''

d.keys()
d.values()
'''to get keys and values
Gives a list of keys and values in a dictionary'''

d.items() #to get both keys and values
