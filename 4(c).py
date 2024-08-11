def sort_dict_by_key(input_dict):
    sorted_dict = dict(sorted(input_dict.items()))
    return sorted_dict

def sort_dict_by_value(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
    return sorted_dict

my_dict = {
    'apple': 3,
    'banana': 1,
    'cherry': 2,
    'date': 4
}

sorted_by_key = sort_dict_by_key(my_dict)
print("Sorted by Key:")
print(sorted_by_key)

sorted_by_value = sort_dict_by_value(my_dict)
print("\nSorted by Value:")
print(sorted_by_value)
