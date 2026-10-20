# Radix Sort Implementation

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"Original array: {myArray}")
# radixArray = [[], [], [], [], [], [], [], [], [], []] # or
radixArray = [[] for _ in range(10)]
maxVal = max(myArray)
exp = 1

while maxVal // exp > 0: # In Python, // means floor division. It divides and rounds the result down to the nearest whole number

    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)

    exp *= 10

print(f"Sorted array: {myArray}")

# On line 10, we use floor division ("//") to divide the maximum value 802 by 1 the first time the while loop runs, 
# the next time it is divided by 10, and the last time it is divided by 100. When using floor division "//", 
# any number beyond the decimal point are disregarded, and an integer is returned.

# On line 14, it is decided where to put a value in the radixArray based on its radix, or digit in focus. 
# For example, the second time the outer while loop runs exp will be 10. 
# Value 170 divided by 10 will be 17. The "%10" operation divides by 10 and returns what is left. 
# In this case 17 is divided by 10 one time, and 7 is left. So value 170 is placed in index 7 in the radixArray.