# Arrays

An array is a data structure used to store multiple elements. Arrays are used by many algorithms.

In Python, an array can be created like this:

```python
my_array = [7, 12, 9, 4, 11]
```

Arrays are indexed, meaning that each element in the array has an index, a number that says where in the array the element is located. The programming languages in this tutorial (Python, Java, and C) use zero-based indexing for arrays, meaning that the first element in an array can be accessed at index 0.

## Algorithm: Find The Lowest Value in an Array

How it works:

- Go through the values in the array one by one.
- Check if the current value is the lowest so far, and if it is, store it.
- After looking at all the values, the stored value will be the lowest of all values in the array.

## Implementation

Before implementing the algorithm using an actual programming language, it is usually smart to first write the algorithm as a step-by-step procedure.

If you can write down the algorithm in something between human language and programming language, the algorithm will be easier to implement later because we avoid drowning in all the details of the programming language syntax.

- Create a variable 'minVal' and set it equal to the first value of the array.
- Go through every element in the array.
- If the current element has a lower value than 'minVal', update 'minVal' to this value.
- After looking at all the elements in the array, the 'minVal' variable now contains the lowest value.

You can also write the algorithm in a way that looks more like a programming language if you want to, like this:

```
Variable 'minVal' = array[0]
For each element in the array
    If current element < minVal
        minVal = current element
```

**Note:** The two step-by-step descriptions of the algorithm we have written above can be called 'pseudocode'. Pseudocode is a description of what a program does, using language that is something between human language and a programming language.

## Algorithm Time Complexity

When exploring algorithms, we often look at how much time an algorithm takes to run relative to the size of the data set.
