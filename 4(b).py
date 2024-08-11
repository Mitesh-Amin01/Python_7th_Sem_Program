my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

my_dict['age'] = 31
print("\nAfter changing 'age' to 31:")
print(my_dict)

if 'city' in my_dict:
    del my_dict['city']
print("\nAfter deleting 'city':")
print(my_dict)

my_dict['country'] = 'USA'
print("\nAfter adding 'country':")
print(my_dict)

removed_value = my_dict.pop('age')
print("\nRemoved 'age' using pop():")
print(my_dict)
print("Removed value:", removed_value)