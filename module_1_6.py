# 2
my_dict = {'Stas': 1999, 'Oleg': 1995, 'Polina': 2005}
print(my_dict)
Polina_value = my_dict.pop('Polina')
print(Polina_value)
print(my_dict.get('Marat'))
my_dict.update({'David': 1999,
                'Emily': 1998})
print(my_dict)
del my_dict['Oleg']
print(my_dict)

#3
my_set = {5, 7, 9, 15, 14, 12, False, 3.87, 8, 5, 9, 7, 12, 7, 12, 9}
print(my_set)
my_set.update({20, 40})
print(my_set)
my_set.remove(15)
print(my_set)
