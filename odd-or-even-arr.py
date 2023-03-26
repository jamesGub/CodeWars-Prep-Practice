#Return whether an array is even or odd. 
"""
Prompt: 
Task:

Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).
Examples:

Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"
"""
#Code
def odd_or_even(arr):
    new_arr = sum(arr) 
    if new_arr % 2 == 0: 
        return "even"
    else:
        return "odd"
#Simple check for an even array, if not, return odd. 
