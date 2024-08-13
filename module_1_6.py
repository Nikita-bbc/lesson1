# dictionary
my_dict = {'Alexey': 2001, 'Vladimir': 1997}
print('Dict', my_dict)
print('Exciting value:', my_dict['Alexey'])
print('Not existing value:', my_dict.get('Pasha'))
my_dict.update({'Pasha': 2005, 'Igor': 2000})
a = my_dict.pop('Vladimir')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
# set
my_set = {1, 2, 3, 2, 1, 2, 3, 'dance', 'Name'}
print('Set:', my_set)
my_set.update({4, 8})
my_set.discard(1)
print('Modified set:', my_set)

