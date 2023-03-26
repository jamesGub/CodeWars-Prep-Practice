#Coding a like tracker, such as who likes a post on social media. 
"""
Prompt: 
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
"""
#Code: 
def likes(names):
    likable = len(names)
    if likable == 0:
        return "no one likes this"
    elif likable == 1:
        return f"{names[0]} likes this"
    elif likable == 2: 
        return f"{names[0]} and {names[1]} like this"
    elif likable == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif likable == 4: 
        return f"{names[0]}, {names[1]} and 2 others like this"
    else:
        likers = likable - 2
        return f"{names[0]}, {names[1]} and {likers} others like this"
    pass
  #Use f strings to return the given name in the list. 
  #To increase the number at the end, instead of using a for loop we can simply
  #subtract two from the list to get the correct amount. 
