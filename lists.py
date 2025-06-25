#lits[]
fruits = ["apple", "banana" , "cherry", "date", "elderberry"]
print(fruits[0])  # Accessing the first element

fruits[1] = "kiwi"  # Modifying the second element
print (fruits)


#addind and removing items
fruits = ["apple", "banana" , "cherry", "date", "elderberry"]

fruits.append("fig")  # Adding an item to the end
print(fruits)

fruits.insert(2, "grape")  # Inserting an item at index 2
print(fruits)

fruits.remove("date")  # Removing an item by value
print(fruits)

fruits.sort()  # Sorting the list
print(fruits)
fruits.reverse()  # Reversing the list
print(fruits)   


