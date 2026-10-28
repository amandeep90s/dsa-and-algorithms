# Queues

A queue is a data structure that can hold many elements.

Think of a queue as people standing in line in a supermarket.

The first person to stand in line is also the first who can pay and leave the supermarket. This way of organizing elements is called FIFO: First In First Out.

Basic operations we can do on a queue are:

1. **Enqueue**: Adds a new element to the queue.
2. **Dequeue**: Removes and returns the first (front) element from the queue.
3. **Peek**: Returns the first element in the queue.
4. **isEmpty**: Checks if the queue is empty.
5. **Size**: Finds the number of elements in the queue.

## Queue Implementation using Arrays

To better understand the benefits with using arrays or linked lists to implement queues, you should check out this page that explains how arrays and linked lists are stored in memory.

Reasons to implement queues using arrays:

- **Memory Efficient:** Array elements do not hold the next elements address like linked list nodes do.
- **Easier to implement and understand:** Using arrays to implement queues require less code than using linked lists, and for this reason it is typically easier to understand as well.
  Reasons for not using arrays to implement queues:

Reasons for not using arrays to implement queues:

- **Fixed size:** An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements. And resizing an array can be costly.
- **Shifting cost:** Dequeue causes the first element in a queue to be removed, and the other elements must be shifted to take the removed elements' place. This is inefficient and can cause problems, especially if the queue is long.
- **Alternatives:** Some programming languages have built-in data structures optimized for queue operations that are better than using arrays.

## Queue Implementation using Linked Lists

Reasons for using linked lists to implement queues:

- **Dynamic size:** The queue can grow and shrink dynamically, unlike with arrays.
- **No shifting:** The front element of the queue can be removed (dequeue) without having to shift other elements in the memory.

Reasons for not using linked lists to implement queues:

- **Extra memory:** Each queue element must contain the address to the next element (the next linked list node).
- **Readability:** The code might be harder to read and write for some because it is longer and more complex.
