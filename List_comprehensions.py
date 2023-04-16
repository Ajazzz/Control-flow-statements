List comprehensions provide a concise way to create lists based on existing lists. They consist of an expression followed by a for clause and optionally one or more if clauses. 
For example, the following code creates a list of squares of the numbers from 1 to 10:

squares = [x**2 for x in range(1, 11)]
print(squares)

Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
