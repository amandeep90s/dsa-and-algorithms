# Selection sort: find the smallest remaining value and move it to the front.
my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

# Each pass places the smallest unsorted value at position i.
for i in range(n - 1):
    min_index = i

    # Search the unsorted portion for its smallest value.
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j

    # Remove the minimum and insert it at the start of the unsorted portion.
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print(f"Sorted array: {my_array}")

# This version uses swapping instead of removing and inserting values.
my_array_2 = [64, 34, 25, 5, 22, 11, 90, 12]

x = len(my_array_2)

# At each position, find the smallest value from i onward.
for i in range(x):
    min_index = i
    for j in range(i + 1, x):
        if my_array_2[j] < my_array_2[min_index]:
            min_index = j

    # Put the smallest value found into position i.
    my_array_2[i], my_array_2[min_index] = my_array_2[min_index], my_array_2[i]

print(f"Sorted array 2: {my_array_2}")