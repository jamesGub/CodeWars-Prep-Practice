#Find a way to reverse the given string parameter in the function.
"""
Prompt: 
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'

"""

#Code: 
def solution(string):
    reversal = string[::-1]
    return reversal
 #We can backwards slice the string to make it "reversed" since there is no built in function. 
