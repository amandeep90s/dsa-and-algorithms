# Linked Lists Types

## Types of Linked Lists

There are three basic forms of linked lists:

1. Singly linked lists
2. Doubly linked lists
3. Circular linked lists

A **singly linked** list is the simplest kind of linked lists. It takes up less space in memory because each node has only one address to the next node, like in the image below.

A **doubly linked** list has nodes with addresses to both the previous and the next node, like in the image below, and therefore takes up more memory. But doubly linked lists are good if you want to be able to move both up and down in the list.

A **circular linked list** is like a singly or doubly linked list with the first node, the "head", and the last node, the "tail", connected.

In **singly** or **doubly linked lists**, we can find the start and end of a list by just checking if the links are null. But for circular linked lists, more complex code is needed to explicitly check for start and end nodes in certain applications.

Circular linked lists are good for lists you need to cycle through continuously.

> **Note**: What kind of linked list you need depends on the problem you are trying to solve.
