Zip:
The zip function is a built-in function that allows you to iterate over two or more sequences in parallel,
i.e. iterating over the corresponding elements of each sequence at the same time. 

For example:

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)
    
Output:

Alice 25
Bob 30
Charlie 35






