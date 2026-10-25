# Linked Lists Operations

Basic things we can do with linked lists are:

1. Traversal
2. Remove a node
3. Insert a node
4. Sort

## Traversal of a Linked List

Traversing a linked list means to go through the linked list by following the links from one node to the next.

Traversal of linked lists is typically done to search for a specific node, and read or modify the node's content, remove the node, or insert a node right before or after that node.

To traverse a singly linked list, we start with the first node in the list, the head node, and follow that node's next link, and the next node's next link and so on, until the next address is null.

## Find The Lowest Value in a Linked List

Let's find the lowest value in a singly linked list by traversing it and checking each value.

Finding the lowest value in a linked list is very similar to how we found the lowest value in an array, except that we need to follow the next link to get to the next node.

## Delete a Node in a Linked List

In this case we have the link (or pointer or address) to a node that we want to delete.

It is important to connect the nodes on each side of the node before deleting it, so that the linked list is not broken.

So before deleting the node, we need to get the next pointer from the previous node, and connect the previous node to the new next node before deleting the node in between.

In a singly linked list, like we have here, to get the next pointer from the previous node we actually need traverse the list from the start, because there is no way to go backwards from the node we want to delete.

Also, it is a good idea to first connect next pointer to the node after the node we want to delete, before we delete it. This is to avoid a 'dangling' pointer, a pointer that points to nothing, even if it is just for a brief moment.

## Insert a Node in a Linked List

Inserting a node into a linked list is very similar to deleting a node, because in both cases we need to take care of the next pointers to make sure we do not break the linked list.

To insert a node in a linked list we first need to create the node, and then at the position where we insert it, we need to adjust the pointers so that the previous node points to the new node, and the new node points to the correct next node.

## Time Complexity of Linked Lists Operations

Here we discuss time complexity of linked list operations, and compare these with the time complexity of the array algorithms that we have discussed previously in this tutorial.

Remember that time complexity just says something about the approximate number of operations needed by the algorithm based on a large set of data n , and does not tell us the exact time a specific implementation of an algorithm takes.

This means that even though linear search is said to have the same time complexity for arrays as for linked list: O(n), it does not mean they take the same amount of time. The exact time it takes for an algorithm to run depends on programming language, computer hardware, differences in time needed for operations on arrays vs linked lists, and many other things as well.

Linear search for linked lists works the same as for arrays. A list of unsorted values are traversed from the head node until the node with the specific value is found. Time complexity is O(n).

Binary search is not possible for linked lists because the algorithm is based on jumping directly to different array elements, and that is not possible with linked lists.

Sorting algorithms have the same time complexities as for arrays, and these are explained earlier in this tutorial. But remember, sorting algorithms that are based on directly accessing an array element based on an index, do not work on linked lists.
