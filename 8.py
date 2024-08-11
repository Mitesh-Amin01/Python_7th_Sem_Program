my_tuple = (1, 2, 3, 4, 5)

sliced_tuple = my_tuple[1:4] 
print("Sliced Tuple:", sliced_tuple)

new_tuple = my_tuple + (6, 7, 8)
print("New Tuple:", new_tuple)

deleted_tuple = my_tuple[:2] + my_tuple[3:]
print("Deleted Tuple:", deleted_tuple)

element = my_tuple[2]  
print("Element at index 2:", element)

index = my_tuple.index(4)
print("Index of 4:", index)

exists = 6 in my_tuple
print("Does 6 exist in the tuple?", exists)
