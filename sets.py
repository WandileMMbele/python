#sets{}
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.add(6)  # Adding an element
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3)  # Removing an element
print(my_set)  # Output: {1, 2, 4, 5, 6}

#operations on sets
set1 = {1, 2, 3}
set2 = {3, 4, 5} 

# Union of sets
union_set = set1.union(set2)  # OR set_union = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of sets
inter_set = set1.intersection(set2)  # OR set_intersection = set1 & set2
print(inter_set)  # Output: {3}

# Difference of sets
diff_set = set1.difference(set2)  # OR set_difference = set1 - set2
print(diff_set)  # Output: {1, 2}