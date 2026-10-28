# Merge Sort

The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, and then building the array back together the correct way so that it is sorted.

**Divide:** The algorithm starts with breaking up the array into smaller and smaller pieces until one such sub-array only consists of one element.

**Conquer:** The algorithm merges the small pieces of the array back together by putting the lowest values first, resulting in a sorted array.

The breaking down and building up of the array to sort the array is done recursively.

> **How it works:**
>
> 1. Divide the unsorted array into two sub-arrays, half the size of the original.
> 2. Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
> 3. Merge two sub-arrays together by always putting the lowest value first.
> 4. Keep merging until there are no sub-arrays left.

## Merge Sort without Recursion

Since Merge Sort is a divide and conquer algorithm, recursion is the most intuitive code to use for implementation. The recursive implementation of Merge Sort is also perhaps easier to understand, and uses less code lines in general.

But Merge Sort can also be implemented without the use of recursion, so that there is no function calling itself.

## Merge Sort Time Complexity

The time complexity for Merge Sort is O(n⋅log n)

And the time complexity is pretty much the same for different kinds of arrays. The algorithm needs to split the array and merge it back together whether it is already sorted or completely shuffled.

If we hold the number of values n fixed, the number of operations needed for the "Random", "Descending" and "Ascending" is almost the same.

Merge Sort performs almost the same every time because the array is split, and merged using comparison, both if the array is already sorted or not.
