''' Generator Expressions:
Generator expressions are similar to list comprehensions, but they return an iterator instead of a list. 
This can be more memory-efficient when dealing with large amounts of data.''' 
For example, 

The following code creates a generator that generates squares of the numbers from 1 to 10:


squares = (x**2 for x in range(1, 11))
for square in squares:
    print(square)
    
Output:


1
4
9
16
25
36
49
64
81
100
