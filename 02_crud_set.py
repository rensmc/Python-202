set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# add

set_countries.add('pe')
print(set_countries)

# update

set_countries.update({'ar', 'ecua'})
print(set_countries)

# remove 

set_countries.remove('col')
set_countries.remove('ar')
print(set_countries)

#set_countries.remove('arg') #Shows error: 'arg' does not exist.
set_countries.discard('arg') #Ignores error.

set_countries.add('arg')
print(set_countries)

set_countries.clear() #wipe
print(set_countries)
print(len(set_countries))

