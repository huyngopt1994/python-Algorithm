# python-Algorithm

## Introduction

This is repo to store solutions, my learning about data structure and algorithms from multiple sources.
## Knowledge
### String
####What
####Why/When
####How
### Array
####What
####Why/When
####How
### Linked List
####What
####Why/When
####How
#### Single Linked List
####What
####Why/When
####How
#### Double Linked List
####What
####Why/When
####How
### Hash table
####What
####Why/When
####How
### Stack/Queue/Heap
Stack is data structure first in last out , This data structure was used in storing memory 
Implement : 
1.We can use a list to implement stack :
 Use append to store to a list
 Use pop to get value from a list
Using 
Queue is data structure first in first out. This data structure mainly was used in scheduling tasks
Implement : We can use 2 ways to implement 
1. Using list : 
- When we want to insert a new , use insert(0,item) => but it's a bad way because it's O(n) algorithm 
when we insert or delete at the begining, every item have to move and reindex 
- Use pop to get value from a list
Because of this, please use `collections.deque`, In short this data structure will make insert or delete at beginning nearly O(1)
Read this link for get more useful information `https://docs.python.org/2/library/collections.html#collections.deque`
Step:
+ Insert data : using `appendleft`
+ Remove data : using `pop`

### Binary Tree
####What
####Why/When
####How
#### Binary Tree Search
####What
####Why/When
####How
### Sorting
####What
####Why/When
####How
### Recursion
#### Stack 
Stack is the data structure (FIFO), This data structure was used mainly for storing memory
When function was called they will push to stack, and they this fuction finised it will be removed from this stack

Stack and Heap was stored in RAM
1. Linear Recursion / De qui tuyen tinh

A linear recursive function is a function that only makes a single call to itself each time the function runs
2. Binary Recursive / De qui nhi phan

Some recursive functions don't just have one call to themself, they have two (or more). Functions with two recursive calls are referred to as binary recursive functions.

### Matrix( 2 dimensional array)
1. Check follow the row
2. Check follow the column
3. Check follow the border
The first row a[0][j], the last row a[n-1][j] , a[i][0] & a[i][-1] if  0 <i < n-1 (n is the number of rows )
4. Check follow principal diagonal
We will loop for per row : and get matrix[i][i] (i is the index of current row)
5. Check follow secondary diagonal
We will loop for per row : and get matrix[i][n-i-1] (i is the index of current row, n is the the number of rows)
### Two Pointer
####What
####Why/When
####How
### Bit manipulation
####What
####Why/When
####How
### BackTracking
####What
####Why/When
####How
### Breath First Search
Use breath First Search to find the shortest path, implement on graph data 
They will answer 2 questions :
1. If have any path from node `A` to node `B`
2. What is the shortest path from node `A` to node `B`.
### Deep First Search
### Graph
It's data structure which include nodes and edge,(they are a set of connection)
 
`node a` have arrows to `node b` and `node c` => `node b` and `node c` are `node a` neighbours
1. Direct graph is only one way relationship , it's meaning some nodes have arrows toward them, but they don't have arrow
for another nodes
2. 
