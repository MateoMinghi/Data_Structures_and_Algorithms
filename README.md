<div align="center">
  <h1>Data Structures and Algorithms</h1>
</div>

This repository contains information regarding data structures and common algorithms. 

The content of this repository is inspired by Udacity's course on Data Structures and Algorithms with Python, as well as MANY other resources.

# Data Structures

Data structures are ways to organize and store data in order to use it in a more efficient way.

We can divide data structures into three categories: list-based collections, hashes and graphs. 

*It is important to point out that there are many more data structures, but the ones mentioned here are the most common ones.*

### List-Based Collections: 
- [Arrays](#Arrays)

- Linked Lists

- Stacks

- Queues

### Hashes:
- Hash Tables

### Graphs:
- Trees

- Binary Trees

- Binary Search Trees

- Graphs

## Arrays
Oversimplifying its definition, we can call an array a type of list. 

In much more depth, arrays are chuncks of memory that store indexed series of data. 

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/arrays.jpg" width="60%"/></p> 


Depending on the programming language, arrays can store different data types, can have fixed sizes and can store duplicated values. But, again, depends on the language.

We acces its values with indexes, starting by 0.

-Accesing an element: O(1)

-Searching for an element: O(n)

-Inserting an element: O(n)

## Linked Lists
A linked list is a group of nodes that have some knowledge on the next element. 

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/linked_list.png" width="70%"/></p> 


Linked lists are composed by nodes and pointers. The node is where the data is stored, and a pointer is a reference to the next node. We can have doubly linked lists or circular linked lists, depending on the pointers.

<p align="center"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/pointer.png" width="200"/></p> 


The first node is called 'Head' and the last node is called 'Tail'. If the value of a node is empty, it's called Null.

We use linked lists over arrays for many different reasons. We can insert elements in constant time and are useful for implementing other data structures.


-Accesing an element: O(n)

-Searching for an element: O(n)

-Inserting an element: O(1)

## Doubly-Linked List

It is just as a linked list, but contains an extra pointer.

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/doubly_linked_list.png" width="80%"/></p> 


This particular type of linked list is very useful for implementing trees and other data structures, but the main reason for using a doubly-linked list over a singly-linked list, is that you can traverse in both directions, instead of just one.

-Accesing an element: O(n)

-Searching for an element: O(n)

-Inserting an element: O(1)


## Stacks
Stacks are a type linear data structure that follows the particular order in which elements are added.

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/stacks.png" width="60%"/></p> 


Stacks can have a Last In, First Out (LIFO) order; or a First In, Last Out (FILO) order. 

These can be extremely useful for creating things in which the order of insertion of elements does matter, such as a news feed.

Stacks can be implemented with arrays or linked lists.
 

-Accesing an element: O(n)

-Searching for an element: O(n)

-Inserting an element: O(1)


## Queues
Queues are really similar to stacks, but unlike them, in a queue the last element goes first.

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/queue.png" width="60%"/></p> 

-enqueue = add an element

-dequeue = remove an element

These can be implemented with arrays and linked lists.

-Accesing an element: O(n)

-Searching for an element: O(n)

-Inserting an element: O(1)


## Hash Tables
A hash table is an associative data structure. It relates a key with a value through hash funcitons.

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/hash_table.png" width="350"/></p> 


Hash tables do not allow duplicate values, but the best thing about using hash tables is that we can insert elements in constant time.

-modifying an element: O(1)

-Searching for an element: O(n)

-Inserting an element: O(1)

But that is not the end of the story. In order to assign keys to values, hash functions are used. These have the purpose of transforming a value into one that can be stored and consulted easily.
 
<p align="center"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/hash_function.png" width="50%"/></p> 


You can store those values in an array, and the index in which the element is going to be found in is also generated by the hash function. 

- must avoid collisions, which is assigning two or more values in the same index
- bucket = where the info is stored in a hash table
- load factor = number of imputs/ number of buckets (important for costs in memory)


## Trees
A tree is just a type of graph. Graph theory is slightly more complex, so I will make a repository on that later. 

Trees are collections of nodes that are arranged in hierarchical order. Nodes can have children. A tree always starts from a root node. Outermost nodes with no children are called leaves.

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/trees.png" width="350"/></p> 


Rules of trees:

- must be completely connected
- if you start off by the root, you must be able to reach any node
- nodes can be parents and children at the same time
- can't have any cycles (one of the main differences between trees and graphs) 

In order to traverse through a tree, we can use DFS and BFS algorithms.

Trees can be implemented with linked lists

-Accesing an element: O(log (n))

-Searching for an element: O(log (n))

-Inserting an element: O(log (n))


## Binary Trees
They are just like trees, but a parent node can have a maximum of two children.

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/binary_tree.png" width="350"/></p> 


We can call the children 'left child' and 'right child'.

A binary tree can be full, complete, degenerate, perfect or balanced

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/types_trees.png" width="80%"/></p> 



-Accesing an element: O(log (n))

-Searching for an element: O(n)

-Inserting an element: O(log (n))

## Binary Search Trees
Binary Search Trees (BST not BTS like the Kpop band) are types of binary trees that are arranged in a particular way, so that the left child or the left subtree of a parent has smaller values than it; but the right child or right subtree has bigger values than it. 

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/binary_search_tree.png" width="350"/></p> 


-Accesing an element: O(log (n))

-Searching for an element: O(log (n))

-Inserting an element: O(log (n))

# Algorithms
An algorithm could be defined as a series of instructions to solve a problem.

*These problems can go from sorting an array, to finding the shortest path in weighted graphs*

In order to measure the efficiency of an algorithm, we use notations. The most common one is the big O notation.

The O notation describes the relationship between the time an algorithm takes to be completed and the size of the input data.

Say that we want to scan an array using a linear search algorithm. This algorithm iterates over every element inside of the array in order to fin the desired value. The number of iterations it has to do is the same as the number of elements insde of the array, so we say it has a complexity of O(n), "n" being the size of the array.  

Its extremely difficult to know the exact time an algorithm takes to run, since it depends on factors such as the computer's power, the programming language or the compiler/interpreter. Therefore we use aproximations like the O notation.

<p align="left"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/algorithmic_complexity.png" width="350"/></p> 

Algorithmic complexities in order (best to worst)

1. O(1) - constant time/space
2. O(log (n)) - logarithmic
3. O(n) - linear time/space
4. O(n log(n))
5. O(n^2)

## Binary Search
This is one of the most common algorithms for finding a particular element inside a data structure.

Binary search is a divide an conquer algorithm. 

Basically, what it does, is that it divides a sorted array into two parts. Then search for the element in the left side. If it isn't located in the left side, it means that it is bigger, therefore we search in the right side. We keep doing that until we find the desired item.

<p align="center"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/binary_search.png" width="350"/></p> 


- O(log (n))


## Selection Sort

As it was mentioned, binary search has to be executed on a sorted array. But what happens if the array isn't sorted? We can sort it with algorithms.

One of the most basic ones is called selection sort. What it does is that it scans throug an unsorted array, finds the smallest value, and places it at the very beginning of the array. That means that we have two sides of the array: the sorted part and the unsored part. We keep doing that until there are only values inside the sorted part.

<p align="center"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/selection_sort.png" width="350"/></p> 


- O(n^2)


## Merge Sort

Selection sort is very inneficient with big arrays. So we need to find a better solution. 

We can use another divide and conquer algorithm, called merge sort. It divides an array into two halves, calls itself for the two halves, and then merges the two sorted halves. 

<p align="center"> <img src="https://github.com/MateoMinghi/Data_Structures_and_Algorithms/blob/main/imgs/merge_sort.png" width="350"/></p> 


-O(n log(n))
