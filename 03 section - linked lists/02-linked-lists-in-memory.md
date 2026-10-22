# Linked Lists in Memory

## Computer Memory

To explain what linked lists are, and how linked lists are different from arrays, we need to understand some basics about how computer memory works.

Computer memory is the storage your program uses when it is running. This is where your variables, arrays and linked lists are stored.

## Arrays in Memory

To understand linked lists, it is useful to first know how arrays are stored in memory.

Elements in an array are stored contiguously in memory. That means that each element is stored right after the previous element.

The image below shows how an array of integers myArray = [3,5,13,2] is stored in memory. We use a simple kind of memory here with two bytes for each integer, like in the previous example, just to get the idea.

The computer has only got the address of the first byte of myArray, so to access the 3rd element with code myArray[2] the computer starts at 0x7F23 and jumps over the two first integers. The computer knows that an integer is stored in two bytes, so it jumps 2x2 bytes forward from 0x7F23 and reads value 13 starting at address 0x7F27.

When removing or inserting elements in an array, every element that comes after must be either shifted up to make place for the new element, or shifted down to take the removed element's place. Such shifting operations are time consuming and can cause problems in real-time systems for example.

## Linked Lists in Memory

Instead of storing a collection of data as an array, we can create a linked list.

Linked lists are used in many scenarios, like dynamic data storage, stack and queue implementation or graph representation, to mention some of them.

A linked list consists of nodes with some sort of data, and at least one pointer, or link, to other nodes.

A big benefit with using linked lists is that nodes are stored wherever there is free space in memory, the nodes do not have to be stored contiguously right after each other like elements are stored in arrays. Another nice thing with linked lists is that when adding or removing nodes, the rest of the nodes in the list do not have to be shifted.
