values = []
for i in range(5):
    value = int(input(f"Enter integer value {i + 1}: "))
    values.append(value)
    
sorted_values = sorted(values)

print("Sorted values:", sorted_values)
