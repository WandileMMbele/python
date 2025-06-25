#tuples()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Accessing the first element 
print(my_tuple[2])  # Slicing the tuple from index 1 to 3  
print(my_tuple[-1])  # Accessing the last element
# Tuples are immutable, so we cannot modify them

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# Concatenating tuples
tuple3 = tuple1 + tuple2 #OR con_tulpe = tuple1.__add__(tuple2)  
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)
# Repeating tuples
tuple4 = tuple1 * 2    #or rep_tuple = tuple1.__mul__(2) 
print(tuple4)  # Output: (1, 2, 3, 1, 2, 3)
