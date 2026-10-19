my_array = [7, 45, 8, 90, 34, 88, 56, 3, 9, 7]

minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print(f"Lowest value: {minVal}")