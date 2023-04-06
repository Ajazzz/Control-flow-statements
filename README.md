# Control-flow-statements
Conditional statements | Loop statements | Break and Continue statements


Control flow statements are used to control the order in which the program executes its instructions. 
In Python, there are several types of control flow statements, including:

### 1). Conditional statements:
Conditional statements allow the program to execute different blocks of code based on the evaluation of a boolean expression. 
The most commonly used conditional statement in Python is the "if" statement.


### 2). Loop statements:
Loop statements are used to repeatedly execute a block of code until a certain condition is met. 
Python has two main loop statements: ``` "for" ``` and ``` "while" ```.

```ruby
# For loop
for i in range(1, 11):
    print(i, end = ' ')
```

```#OUTPUT  1 2 3 4 5 6 7 8 9 10  ```

```ruby
# while loop
x=0
while x<10:
    print(x)
    x+=1
```


```
#OUTPUT
0
1
2
3
4
5
6
7
8
9
```

### 3). Break and Continue statements:
```"break"``` and ```"continue"``` statements are used inside loops to alter their behavior. 
```"break"``` statement is used to exit a loop prematurely, while "continue" statement is used to skip to the next iteration of the loop.

```ruby
x = 0

while x<10:
    print(x)
    x+=1
    if x == 5:
        break
    else:
        continue
```


These control flow statements are fundamental building blocks for creating complex programs in Python.
