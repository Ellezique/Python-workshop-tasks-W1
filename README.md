# Python workshop tasks
## Materials to read
Data structures (https://en.wikipedia.org/wiki/List_of_data_structures)
Big O notation (https://en.wikipedia.org/wiki/Big_O_notation)
Computational complexity (https://en.wikipedia.org/wiki/Computational_complexity_theory)
Sequence (https://en.wikipedia.org/wiki/Sequence)
Series (https://en.wikipedia.org/wiki/Series_(mathematics))
Set notation (https://en.wikipedia.org/wiki/Set_notation)
## Algorithms

1. Implement a stack with operations Push, Pop, Max, where each operation takes constant time to complete: O(c)

2. Implement a queue with operations Push, Pop, Max, where each operation takes constant time to complete: O(c)

3. You are given an input string as a sequence of brackets of different types  '(', ')', '[', ']', '{', ‘}’. We need to implement an algorithm that will check if the sequence is correct, i.e. there is a closing bracket for each opening bracket. For example
‘([{}])’ and ‘()()’ are correct, ‘[)’ and ‘[(])’ are not. The algorithm should be of O(n) complexity where n is the length of the input string.

4. You are given a sequencea_1,a_2,...,a_n  ∈N, and S∈N. Implement a program that would find l,r:(1≤l≤r≤n) so that ∑_(i=l)^r a_i=S: O(n)

5. You are given a sequencea_1,a_2,...,a_n  ∈Z. Implement a program that would find l,r:(1≤l≤r≤n) so that ∑_(i=l)^r a_iwould be the maximum possible: O(n)

## Matrices
1. You are given a big matrix and a smaller one, write a function that returns the coordinates of a smaller matrix within a bigger one. Start with 2d and experiment with higher dimensions.
2. You are given a big matrix, a smaller one and a number representing how much to rotate the smaller matrix in multipliers of π radians in increments of 0.5 (0, 0.5, 1, ...). Write a function that returns a copy of a big matrix where the smaller matrix is rotated  accordingly.
3. You are given the size of a matrix (e.g. width and height for 2D) and the coordinate of the start and the end of the line segment. 3. 3.3. Write a function that returns the matrix which has 1 where the line pixels should be and 0 where they shouldn’t. 
Draw the matrix as a graphical output. Start with 2d and experiment with higher dimensions.
4. Same as 3, but now with antialiasing, where the numbers in the resulting matrix represent the pixel transparency.


#### Additional resources used
Algorithms: Question 1
- Runestone Academy, Chapter 4 and specifically 4.5 'Implementing a Stack in Python', https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html 
- Programiz, Python max(),  https://www.programiz.com/python-programming/methods/built-in/max
- https://www.edureka.co/blog/stack-in-python/

