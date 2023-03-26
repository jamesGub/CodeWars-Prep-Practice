#Return the min and max values in a list
"""
Prompt: 
Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.
Examples (Input -> Output)

* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5
"""
#Code
def minimum(arr):
    arr.sort()
    return arr[0]

def maximum(arr):
    arr.sort()
    return arr[-1]
#Very very simple way to get the min max from a list, however
#we do not even need to do 2 functions but for the sake of the problem I did. 
