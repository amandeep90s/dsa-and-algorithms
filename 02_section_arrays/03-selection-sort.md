# Selection Sort

The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

How it works:

1. Go through the array to find the lowest value.
2. Move the lowest value to the front of the unsorted part of the array.
3. Go through the array again as many times as there are values in the array.

## Selection Sort Implementation

To implement the Selection Sort algorithm in a programming language, we need:

1. An array with values to sort.
2. An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. This loop must loop through one less value each time it runs.
3. An outer loop that controls how many times the inner loop must run. For an array with values, this outer loop must run 1 times.

## Selection Sort Shifting Problem

The Selection Sort algorithm can be improved a little bit more. In the code above, the lowest value element is removed, and then inserted in front of the array.

## Solution: Swap Values!

Instead of all the shifting, swap the lowest value (5) with the first value (64) like below.
