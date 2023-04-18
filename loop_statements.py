'''Loop statements in Python are used to repeat a set of instructions a certain number of times or until a certain condition is met. 
There are two main types of loop statements in Python: "for" and "while".

The "for" loop is used to iterate over a sequence (e.g. a list, tuple, or string) or a range of numbers. 

The basic syntax of a for loop is as follows:'''

for item in sequence:
    # do something with item
    
'''   
Here, "item" is a variable that takes on the value of each item in the sequence, one at a time. 
The code inside the loop block is executed once for each item in the sequence.
For example, the following code prints the numbers from 0 to 9:'''    


for i in range(10):
    print(i)
    
'''
The "while" loop is used to repeat a set of instructions while a certain condition is true. 
The basic syntax of a while loop is as follows:'''

#####

while condition:
    # do something
    
########

'''Here, "condition" is a boolean expression that is checked at the beginning of each iteration. 
If the condition is true, the code inside the loop block is executed; otherwise, the loop terminates. '''

''' For example, the following code prints the numbers from 0 to 9 using a while loop:'''

########

i = 0
while i < 10:
    print(i)
    i += 1
    
#######
In this code, the variable "i" is initially set to 0. The condition "i < 10" is checked at the beginning of each iteration. 
As long as the condition is true, the code inside the loop block is executed, which prints the current value of "i" and increments it by 1. 
The loop terminates when "i" becomes 10, because the condition "i < 10" is no longer true.




Examples:
########

# for loop
for i in range(10):
    print(i)

# while loop
x = 0
while x < 10:
    print(x)
    x += 1

########

string = "Hello, World!"
for char in string:
    print(char)

########

string = "Hello, World!"
for i in range(len(string)):
    print(string[i])
    
########    
Using a while loop, you can loop through the characters in a string until a certain condition is met. 
Here is an example:

string = "Hello, World!"
i = 0
while i < len(string):
    print(string[i])
    i += 1





































































