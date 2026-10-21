# Linear Search

The Linear Search algorithm searches through an array and returns the index of the value it searches for.

This algorithm is very simple and easy to understand and implement. If the array is already sorted, it is better to use the much faster Binary Search algorithm.

A big difference between sorting algorithms and searching algorithms is that sorting algorithms modify the array, but searching algorithms leave the array unchanged.

> **How it works:**
>
> 1. Go through the array value by value from the start.
> 2. Compare each value to check if it is equal to the value we are looking for.
> 3. If the value is found, return the index of that value.
> 4. If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.

## Linear Search Implementation

To implement the Linear Search algorithm we need:

1. An array with values to search through.
2. A target value to search for.
3. A loop that goes through the array from start to end.
4. An if-statement that compares the current value with the target value, and returns the current index if the target value is found.
5. After the loop, return -1, because at this point we know the target value has not been found.

## Linear Search Time Complexity

If Linear Search runs and finds the target value as the first array value in an array with n values, only one compare is needed.

But if Linear Search runs through the whole array of n values, without finding the target value, n compares are needed.

This means that time complexity for Linear Search is O(n)
