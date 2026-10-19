# Bubble Sort

Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

Each value in the array is represented by a column.

The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.

## How it works:

1. Go through the array, one value at a time.
2. For each value, compare the value with the next value.
3. If the value is higher than the next one, swap the values so that the highest value comes last.
4. Go through the array as many times as there are values in the array.

## Bubble Sort Implementation

To implement the Bubble Sort algorithm in a programming language, we need:

1. An array with values to sort.
2. An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
3. An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.

## Bubble Sort Time Complexity

The Bubble Sort algorithm loops through every value in the array, comparing it to the value next to it. So for an array of values, there must be such comparisons in one loop.

And after one loop, the array is looped through again and again times.
