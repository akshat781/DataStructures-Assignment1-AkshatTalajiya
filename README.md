# DataStructures-Assignment1-AkshatTalajiya
# DataStructures-Assignment1-AkshatTalajiya

**Name:** Akshat Talajiya  
**Student ID:** [Your Student ID]

## Overview

This repository contains solutions to the five coding challenges from Assignment 1 in the CSD 4464 course, which focuses on various data structures, including arrays, linked lists, stacks, queues, and binary trees.

## Challenges and Approaches

### 1. The Array Artifact
**Approach:**  
I implemented a class `ArtifactVault` to manage an array of ancient artifacts. The methods include adding and removing artifacts, performing linear and binary search. For binary search, the array is kept sorted by artifact age.

**Assumptions/Decisions:**
- I used Python's list to simulate an array.
- The array is of fixed size, and binary search is implemented on the sorted array of artifacts by age.

### 2. The Linked List Labyrinth
**Approach:**  
In this challenge, I used a singly linked list to represent a path in the labyrinth. I implemented methods to add new locations, remove the last location, check for loops (traps), and print the entire path.

**Assumptions/Decisions:**
- Each node in the linked list contains a reference to the next location.
- I implemented Floyd's Cycle Detection Algorithm to detect loops in the list.

### 3. The Stack of Ancient Texts
**Approach:**  
I developed a `ScrollStack` class using a linked list-based stack. The stack operations include push, pop, peek, and checking if a specific scroll exists in the stack.

**Assumptions/Decisions:**
- The stack is implemented using a singly linked list, where each node represents a scroll.
- The stack follows the LIFO principle.

### 4. The Queue of Explorers
**Approach:**  
I implemented a circular queue using an array to manage explorers entering the temple. The methods include enqueueing, dequeueing, checking if the queue is full/empty, and displaying the next explorer.

**Assumptions/Decisions:**
- A fixed-size array is used to simulate the circular queue.
- The queue supports standard circular operations, with pointers tracking the front and rear.

### 5. The Binary Tree of Clues
**Approach:**  
The `ClueTree` class represents a binary tree with methods to insert clues, perform different tree traversals (in-order, pre-order, post-order), find specific clues, and count the total number of clues.

**Assumptions/Decisions:**
- Clues are inserted into the binary tree with the assumption that the clues are unique.

## How to Run the Code

1. Clone this repository to your local machine using:
2. Navigate to the project directory:
3. To run any of the challenges, use Python to execute the corresponding file. For example:
4. Make sure you have Python 3.x installed on your system.