# Merge Sort Implementation

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 # Find the middle index of the array
    leftHalf = arr[:mid] # Split the array into left half
    rightHalf = arr[mid:] # Split the array into right half

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right [j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:]) # Add any remaining elements from the left half
    result.extend(right[j:]) # Add any remaining elements from the right half

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print(f"Sorted array: {sortedArr}")
