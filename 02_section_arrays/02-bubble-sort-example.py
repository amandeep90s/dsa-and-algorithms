# Bubble sort implementation

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

print(f"Sort array: {my_array}")

# Bubble Sort Improvement
# If the algorithm goes through the array one time without swapping any values, 
# the array must be finished sorted, and we can stop the algorithm, like this:
my_array_2 = [7, 3, 9, 12, 11]

n2 = len(my_array_2)

for x in range(n2 - 1):
    swapped = False
    for y in range(n2 - x - 1):
        if my_array_2[y] > my_array_2[y + 1]:
            my_array_2[y], my_array_2[y + 1] = my_array_2[y + 1], my_array_2[y]
            swapped = True
    if not swapped:
        break

print(f"Sort array: {my_array_2}")