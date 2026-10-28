# Insertion Sort Implementation

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(1, n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i - 1, -1, -1):  # range(i - 1, -1, -1) checks indexes backward: from i - 1 down to 0
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)

print(f"Sort array: {my_array}")

# Improved Solution
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            # What is also done in the code above is to break out of the inner loop. 
            # That is because there is no need to continue comparing values when we have already found the correct place for the current value.
            break
    my_array[insert_index] = current_value

print("Sorted array:", my_array)