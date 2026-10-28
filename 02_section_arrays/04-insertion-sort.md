# Insertion Sort

The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.

The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

How it works:

1. Take the first value from the unsorted part of the array.
2. Move the value into the correct place in the sorted part of the array.
3. Go through the unsorted part of the array again as many times as there are values.

## Insertion Sort Implementation

To implement the Insertion Sort algorithm in a programming language, we need:

1. An array with values to sort.
2. An outer loop that picks a value to be sorted. For an array with n values, this outer loop skips the first value, and must run n−1 times.
3. An inner loop that goes through the sorted part of the array, to find where to insert the value. If the value to be sorted is at index i, the sorted part of the array starts at index 0 and ends at index i−1.

## Insertion Sort Improvement

Insertion Sort can be improved a little bit more.

The way the code above first removes a value and then inserts it somewhere else is intuitive. It is how you would do Insertion Sort physically with a hand of cards for example. If low value cards are sorted to the left, you pick up a new unsorted card, and insert it in the correct place between the other already sorted cards.

The problem with this way of programming it is that when removing a value from the array, all elements above must be shifted one index place down:

Removing an element from an array
And when inserting the removed value into the array again, there are also many shift operations that must be done: all following elements must shift one position up to make place for the inserted value.

These shifting operations can take a lot of time, especially for an array with many elements.

Hidden memory shifts: You will not see these shifting operations happening in the code if you are using a high-level programming language such as Python or JavaScript, but the shifting operations are still happening in the background. Such shifting operations require extra time for the computer to do, which can be a problem.

You can read more about how arrays are stored in memory here.

C and Java code examples above and below are the same: The issue of memory shifts happening behind the scenes is only relevant for high-level programming languages like Python or JavaScript, where arrays are dynamic, which means you can easily remove and insert elements. In lower-level programming languages like C and Java, where arrays have a fixed length, elements cannot be removed or inserted. As a result, there are no such memory shifts happening, and therefore the example codes above and below for C and Java remain the same.

## Improved Solution

We can avoid most of these shift operations by only shifting the values necessary:

Moving an element in an array efficiently
In the image above, first value 7 is copied, then values 11 and 12 are shifted one place up in the array, and at last value 7 is put where value 11 was before.

The number of shifting operations is reduced from 12 to 2 in this case.

## Insertion Sort Time Complexity

Insertion Sort sorts an array of n values.

On average, each value must be compared to about n/2 other values to find the correct place to insert it.

Insertion Sort must run the loop to insert a value in its correct place approximately n times.
