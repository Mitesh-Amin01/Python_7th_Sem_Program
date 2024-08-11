def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target_element = 40

result = binary_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
