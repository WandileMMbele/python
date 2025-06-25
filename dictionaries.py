
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict['city'])  # Output: {'name': 'Alice', 'age': 30

# Modifying a value
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Adding a new key-value pair
my_dict['job'] = 'Engineer'
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair
del my_dict['city']
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'job': 'Engineer'}
