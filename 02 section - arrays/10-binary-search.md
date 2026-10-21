# Binary Search

The Binary Search algorithm searches through an array and returns the index of the value it searches for.

Binary Search is much faster than Linear Search, but requires a sorted array to work.

The Binary Search algorithm works by checking the value in the center of the array. If the target value is lower, the next value to check is in the center of the left half of the array. This way of searching means that the search area is always half of the previous search area, and this is why the Binary Search algorithm is so fast.

This process of halving the search area happens until the target value is found, or until the search area of the array is empty.

> How it works:
>
> 1. Check the value in the center of the array.
> 2. If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
> 3. Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
> 4. If the value is found, return the target value index. If the target value is not found, return -1.

## Binary Search Implementation

To implement the Binary Search algorithm we need:

An array with values to search through.

1. A target value to search for.
2. A loop that runs as long as left index is less than, or equal to, the right index.
3. An if-statement that compares the middle value with the target value, and returns the index if the target value is found.
4. An if-statement that checks if the target value is less than, or larger than, the middle value, and updates the "left" or "right" variables to narrow down the search area.
5. After the loop, return -1, because at this point we know the target value has not been found.

## Binary Search Time Complexity

For a more thorough and detailed explanation of Insertion Sort time complexity, visit this page.

Each time Binary Search checks a new value to see if it is the target value, the search area is halved.

This means that even in the worst case scenario where Binary Search cannot find the target value, it still only needs log2n comparisons to look through a sorted array of n values.

Time complexity for Binary Search is O(log2n)

Note: When writing time complexity using Big O notation we could also just have written O(logn), but O(log2n) reminds us that the array search area is halved for every new comparison, which is the basic concept of Binary Search, so we will just keep the base 2 indication in this case.
