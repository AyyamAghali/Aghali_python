# Aghali_python

# task_algorithm

A single Python script that performs three small algorithmic tasks in sequence:

1. **Number check**: Reads a number and prints “Hello” if it’s greater than 7.  
2. **Name check**: Reads a name and prints “Hello, John” if it matches `John`; otherwise, prints “There is no such name.”  
3. **Array filter**: Reads a space-separated list of integers and prints those divisible by 3.





## Given bracket sequence:  "[((())()(())]]"
Can this sequence be considered correct? 
If the answer to the previous question is “no”, then what needs to be changed in it to make it correct? 

# 1. No. In the second parenthesis-group, there are two “(” but three “)”, so at one point you have more closes than opens.

# 2. Remove the extra ')' so each opening parenthesis has a matching closer. For example:  [ ((())) (()) ]. Now every prefix has no more ) than (, and the total counts match.