#Collection for easier code wars questions around the 7 to 8 kyu level. 
"""
8 kyu
Remove First and Last Character
Python:
"""
#Code:
def remove_char(s):
    new_s = s[1:-1]
    return new_s
"""
8 kyu
Find the smallest integer in the array
Python:  
"""
#Code: 
def find_smallest_int(arr):
    arr.sort()
    return arr[0]
"""
8 kyu
Convert a Boolean to a String
Python:
"""
#Code:
def boolean_to_string(b):
    new_b = str(b)
    return f"{b}"
"""
8 kyu
Cat years, Dog years
Python:
"""
#Code
def human_years_cat_years_dog_years(human_years):
    if human_years == 1: 
        catYears = 15
        dogYears = 15
    elif human_years == 2: 
        catYears = 15 + 9
        dogYears = 15 + 9
    else: 
        catYears = 15 + 9 + 4 * (human_years - 2)
        dogYears = 15 + 9 + 5 * (human_years - 2)
        
        
        
    return [human_years, catYears, dogYears]
 """
7 kyu
Number of People in the Bus
Python:
"""
#Code
def number(bus_stops):
    # Start with people on the bus at zero, this will be our integer that we 
    # add and subtract to. 
    
    passengers = 0
    
    for i in bus_stops:
        passengers += i[0]
        
        passengers -= i[1]
        
    return passengers
"""
7 kyu
Beginner Series #3 Sum of Numbers
Python:
"""
#Code
def get_sum(a,b):
    #elif a == b: return a or b
    
    if a == b: 
        return a
    elif a < b:
        return sum(range(a, b + 1))
    else: 
        return sum(range(b, a + 1))
"""
8 kyu
Opposites Attract
Python:
"""
#Code
def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 == 1 or flower1 % 2 == 1 and flower2 % 2 == 0:
        return True
    else:
        return False
"""
7 kyu
Highest and Lowest
Python:
"""
#Code
def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split()]

    # Find the highest and lowest numbers
    highest = max(num_list)
    lowest = min(num_list)
"""
8 kyu
Remove exclamation marks
Python:
"""
#Code
def remove_exclamation_marks(s):
    removable = "!"
    returnable = s.replace(removable, "")
"""
7 kyu
Is this a triangle?
Python:
"""
#Code
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a: 
        return True
    else:
        return False
    return returnable
    return f"{highest} {lowest}"
"""
8 kyu
DNA to RNA Conversion
Python:
"""
def dna_to_rna(dna):
    return dna.replace("T", "U")
"""
8 kyu
Fake Binary
Python:
"""
def fake_bin(x):
    result = ""
    for digit in x:
        if int(digit) < 5:
            result += "0"
        else:
            result += "1"
    return result
"""
8 kyu
You only need one - Beginner
Python:
"""
#Code
def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False
"""
8 kyu
Check same case
Python:
"""
#Code:
def same_case(a, b): 
    #if a and b are lower case
    #   then return a variable containing 1
    # else if a and b are uppercase
    #    then return a variable containing 1
    #else if a or b is uppercase and a or b is lowercase
    #   then return 0
    # else return - 1
    if not a.isalpha() or not b.isalpha():
        return -1
    elif a.islower() == b.islower():
        return 1
    else:
        return 0
"""
7 kyu
Vowel Count
Python:
"""
#Code
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for c in sentence: 
        if c in vowels: 
            count += 1
"""
8 kyu
Returning Strings
Python:
"""
#Code
def greet(name):
    return "Hello, " + name + " how are you doing today?"
"""
8 kyu
Parse nice int from char problem
Python:
"""
#Code
import random
def get_age(age):
    return int(age[0])
    
    return count
"""
8 kyu
Calculate average
Python:
"""
#Code
def find_average(numbers):
    return sum(numbers) / len(numbers)
"""
8 kyu
Beginner Series #2 Clock
Python:
"""
#Code
def past(h, m, s):
    return ((h * 60 + m) * 60 + s) * 1000
"""
7 kyu
Exes and Ohs
Python:
"""
def xo(s):
    s = s.lower() 
    return s.count("x") == s.count("o")
"""
8 kyu
Return Negative
Python:
"""
#Code
def make_negative( number ):
    if number <= 0: 
        return number * 1
    elif number >= 0:
        return number * -1
"""
8 kyu
Remove String Spaces
Python:
"""
#Code
def no_space(x):
    return x.replace(" ", "")
"""
7 kyu
Ones and Zeros
Python:
"""
def binary_array_to_number(arr):
    binary_string = "".join(map(str, arr))
    decimal_num = int(binary_string, 2)
    return decimal_num
"""
8 kyu
Convert a String to a Number!
Python:
"""
#Code
def string_to_number(s):
    return int(s)
"""
8 kyu
Are You Playing Banjo?
Python:
"""
#Code
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
"""
8 kyu
Gravity Flip
Python:
"""
#Code
def flip(d, a):
    a.sort()
    if d == "R":
        a.sort()
    elif d == "L":
        a.reverse()
    return a
"""
8 kyu
Simple multiplication
Python:
"""
#Code
def simple_multiplication(number) :
    
    if (number % 2) == 0: 
        return number * 8
    else:
        return number * 9
"""
8 kyu
Count of positives / sum of negatives
Python:
"""
#Code
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pos_count = sum(1 for num in arr if num > 0)
    neg_sum = sum(num for num in arr if num < 0)
    return [pos_count, neg_sum]
"""
8 kyu
Floating point comparison
Python:
"""
#Code
def approx_equals(a, b):
    return abs(a - b) < 0.001
"""
8 kyu
Beginner Series #1 School Paperwork
Python:
"""
#Code
def paperwork(n, m):
    if n < 0 or m < 0: 
        return 0
    else: 
        return n * m
"""
8 kyu
Convert number to reversed array of digits
Python:
"""
#Code
def digitize(n):

     if n == 0:
        return [0]
     else:
        digits = []
        while n > 0:
            digit = n % 10
            digits.append(digit)
            n //= 10
        return digits
 """
 8 kyu
Century From Year
Python:
"""
#Code
def century(year):
     return (year - 1) // 100 + 1
"""
7 kyu
Printer Errors
Python:
"""
#Code
def printer_error(s):
      # Get the total length of the control string
    total_length = len(s)
    
    # Get the number of errors in the control string
    error_count = sum([1 for c in s if c not in 'abcdefghijklm'])
    
    # Return the error rate as a string
    return f"{error_count}/{total_length}"
"""
8 kyu
Sum Arrays
Python:
"""
#Code
def sum_array(a):
    if not a:
        return 0
    else: 
        return sum(a) 
"""
7 kyu
Sum of odd numbers
Java:
"""
#Code
class RowSumOddNumbers {
    public static int rowSumOddNumbers(int n) {
        int firstNumberInRow = (n * (n - 1)) + 1;
        int sum = 0;
        for (int i = 0; i < n; i++) { 
         sum += firstNumberInRow + (2 * i); 
        }
     return sum;
}
"""
8 kyu
Area or Perimeter
Python:
"""
#Code
def area_or_perimeter(l , w):
    
    
    if (l == w): 
        return l ** 2
    else: 
        return 2 * (l + w)
  }
"""
7 kyu
Valid Parentheses
Python:
"""
#Code
def valid_parentheses(paren_str):
    stellar_array = []
    
    for p in paren_str: 
        if p == "(":
            stellar_array.append(p)
        elif p == ")":
            if not stellar_array:
                return False
            stellar_array.pop()
    return not stellar_array
"""
8 kyu
Invert values
Python:
"""
#Code
def invert(lst):
    return [-n for n in lst]
"""
8 kyu
Convert boolean values to strings 'Yes' or 'No'.
Python:
"""
def bool_to_word(boolean):
    # TODO
    if boolean == True:
        return "Yes"
    else:
        return "No"
"""
8 kyu
Convert a Number to a String!
Python:
"""
#Code:
def number_to_string(num):
    x = num
    new_word = '{}'.format(num)
    return new_word
"""
8 kyu
Abbreviate a Two Word Name
Python:
"""
#Code
def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"
"""
8 kyu
Grasshopper - Personalized Message
Python:
"""
#Code
def greet(name, owner):
    
    if (name == owner):
        return "Hello boss"
    else:
        return "Hello guest"
"""
8 kyu
Byte me!
Python:
"""
#Code
# return the total byte size of the object. 
import sys 
def total_bytes(object):
    x = sys.getsizeof(object)
    return x
 """
 8 kyu
A Needle in the Haystack
Python:
"""
#Code
def find_needle(haystack):

    index = haystack.index("needle")
    
    return "found the needle at position " + str(index)
"""
8 kyu
Counting sheep...
Python:
"""
#Code
def count_sheeps(sheep):
    count = 0
    
    for sheeps in sheep: 
        if sheeps: 
            count += 1
            
    return count
    pass
"""
8 kyu
If you can't sleep, just count sheep!!
Python:
"""
#Code
def count_sheep(n):
    result = ""
    
    for i in range(1, n+1):
        result += str(i) + " sheep..."
        
    return result
"""
8 kyu
Is he gonna survive?
Python:
"""
#Code
def hero(bullets, dragons):
    bullets_needed = dragons * 2
    
    if bullets >= bullets_needed: 
        return True
    else:
        return False
        
"""
7 Kyu
Shortest Word
Python:
"""
#Code
def find_short(s):
    #length()?
    #min()?
    #sort()? 
    #split() turns the strings into a list, then we use the sorted 
    #method defined by length on the list, return the length of the 
    #first word.
    s_list = s.split()
    shortest_word = sorted(s_list, key=len)
    return len(shortest_word[0])
"""
7 Kyu 
Disemvowel Trolls
Python: 
"""
#Code
def disemvowel(string_):
    #Strip()?
    #Special remove methods?
    #Cut out all vowels then return the string
    #as it is.
    #Set the vowels to a tuple
    #Use a for loop, if i is not in vowels
    no_vows = ""
    for i in string_:
        if i not in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            no_vows = no_vows + i
    return no_vows
"""
6 Kyu
Detect Panagram
Python:
"""
#Code
def is_pangram(s):
    #Use a for loop to check for the whole alphabet in the string
    
    #Store the alphabet in a variable
    greek = "abcdefghijklmnopqrstuvwxyz"
    #Use a for loop to track for every letter
    for i in greek: 
        #If all letters are not in the string, its not a panagram
        if i not in s.lower():
            return False
    #If yes, true
    return True
"""
8 Kyu
Beginner - Reduce but Grow
Python: 
"""
#Code
def grow(arr):
    res = 1
    for i in arr: 
            res = res * i
    return res
"""
7 Kyu
String ends with? 
Python:
"""
#Code
def solution(text, ending):
    #Use for loop to see if ending is in text
    #Possible indexing? 
    #If the ending is there, return true
    #Endsiwthmethod
    
    enfin = text.endswith(ending)
    return enfin
    pass
"""
6 Kyu
Break camelCase
Python:
"""
#Code
import re
def solution(s)
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
"""
8 Kyu
Sentence Smash
Python: 
"""
def smash(words):
    return " ".join(words)
"""
8 Kyu
Rock Paper Scissors!
Python: 
"""
#Code
def rps(p1, p2):
    if p1 == "scissors" and p2 =="paper":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 =="rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    else:
        return "Draw!"
 """
 8 Kyu
 Basic Mathematical Operations
 Python: 
 """
#Code
def basic_op(operator, value1, value2):
    if operator == "+": 
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/": 
        return value1 / value2
    else:
        return False
 """
 7 Kyu
 Isograms
 Python:
 """
#Code
def is_isogram(string):
    string = string.lower()
    
    for i in range(len(string)):
        if string.count(string[i]) > 1:
            return False
    return True
"""
6 Kyu
Counting Duplicates
Python: 
"""
#Code
def duplicate_count(text):
    #For loop to iterate 
    #Dictionary to store the amounts, 
    #this will allow us to count the amount of dupes
    #Check got alphabetic and numeric characters
    
    text = text.lower()
    
    dupes = {}
    
    for char in text:
        if char.isalnum():
            if char in dupes: 
                dupes[char] += 1
            else:
                dupes[char] = 1
        
    count = 0
    
    for char in dupes: 
        if dupes[char] > 1:
            count += 1
    return count
"""
7 kyu
Sum of two lowest positive integers
Python: 
"""
#Code 
def sum_two_smallest_numbers(numbers):
    #Start by sorting the array: sort()
    #Add the indices for [0] andn [1]
    
    new_nums = numbers.sort()
    
    result = numbers[0] + numbers[1]
    
    return result
"""
8 kyu
Opposite number
Python: 
"""
#Code
def opposite_number(number):
    if number >= 0:
        return number * -1
    else:
        return number * 1
"""
8 kyu
Quarter of the year
Python:
"""
#Code
def quarter_of(month):
    #month in range of 1-3, 4-6, 7-9, 10-12
    if month in range(1,4):
        return 1
    elif month in range(4,7):
        return 2
    elif month in range(7,10):
        return 3
    elif month in range(10,13):
        return 4
"""
7 Kyu
You're a square!
Python:
"""
#Code
import math

def is_square(n):    
    if n >= 0: 
        root = math.sqrt(n)
        if int(root + 0.5) ** 2 == n: 
            return True
        else:
            return False
    if n < 0:
        return False
#Import math to use the sqrt() function
#Set the square root of n to the root variable
#Make sure the root is set to an integer, otherwise
#you will return a float which is not a perfect square
#if root + 0.5 times itself = n, return true
#if not, return false
#if negative return false, must be done outside of scope
"""
8 kyu
Grasshopper - Grade book
Python: 
"""
#Code
def get_grade(s1, s2, s3):
    summer = s1 + s2 + s3
    avg = summer / 3
    avg = int(avg)
    
    if avg >= 90 and avg <= 100:
        return "A"
    elif avg >= 80 and avg < 90:
        return "B"
    elif avg >= 70 and avg < 80:
        return "C"
    elif avg >= 60 and avg < 70:
        return "D"
    else:
        return "F"
"""
6 kyu
Count the smiley faces!
Python:
"""
#Code
def count_smileys(arr):
    #Set smiley variable to 0 so we can count off it later
    smiley = 0
    
    #Set valid components to a variable
    valid_eyes = [":", ";"]
    valid_nose = ["", "-", "~"]
    valid_mouth = [")", "D"]
    #Use a for loop to iterate the array and search for the valid characters
    for smiles in arr: 
        if len(smiles) == 2:
            if smiles[0] in valid_eyes and smiles[1] in valid_mouth: 
                smiley += 1
        elif len(smiles) == 3:
            if smiles[0] in valid_eyes and smiles[1] in valid_nose and smiles[2] in valid_mouth:
                smiley += 1
    return smiley

#Check for the length and account for smiley faces with or without noses
#If the length is 2, we can assume it has no nose, in which case, we check for the valid variables and add to the smiley count
#If the length is 3, it has a nose, in which case, we do the same thing but this time at the 3 proper indices
#Return the smiley count
"""
7 kyu
List Filtering
Python:
"""
#Code
def filter_list(l):
    #If strings are in l
    #Return the list with no strings
    wo_string = []
    
    for items in l:
        if isinstance(items, (int, float)):
            wo_string.append(items)
        return wo_string
"""
8 kyu
Sum of positive
Python:
"""
#Code
def positive_sum(arr):
    total = 0
    for num in arr: 
        if num > 0: 
            total += num
    return total
"""
8 kyu
Third angle of a triangle
Python:
"""
#Code 
def other_angle(a, b):
    return 180 - (a + b)
#Sum is always 180, subtract a and b from 180 to find the third side
"""
6 kyu
Your order, please
Python:
"""
#Code
def order(sentence):
    #If the string is empty
    if not sentence:
        return ""
    #Create an empty list to store the values
    sen_emp = []
    
    #Loop the numbers 1-9 that will appear in the string, determine the range
    for number in range(1,10):
        #Goes over the string by using split, looping over each word
        for word in sentence.split():
            #if the word contains a number, we append it to the empty list
            if str(number) in word:
                sen_emp.append(word)
                
    #Using join, we can put the sorted numbers into a string and combine with the list.
    return " ".join(sen_emp)
            
"""
7 kyu
Find the stray number
Python:
"""
#Code
def stray(arr):
    #return the one that does not match
    #for loop
    for num in arr:
        #count the number of occurences of the number in the array
        #if the count is not divisible by 2, that means it is the odd one out. 
        if arr.count(num) % 2 != 0:
            return num
"""
8 kyu
Will you make it?
Python:
"""
#Code
def zero_fuel(distance_to_pump, mpg, fuel_left):
    #return true if we have enough gas to the pump
    #We have 2 gallons, with 25 miles per, and the nearest pump is 50 miles away.
    
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False
"""
8 Kyu
Find the first non-consecutive number
Python:
"""
#code
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != 1:
            return arr[i]
    return None
"""
7 kyu
Binary Addition
Python:
"""
#Code
def add_binary(a,b):
    sum = a + b
    return bin(sum)[2:]
#Bin() function returns the binary value, to get rid of the 0b
#we slice the string by 2 by [2:]
"""
6 kyu
Persistent Bugger.
Python:
"""
#Code
def persistence(n):
    count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        num = product
        count += 1
 """
 8 kyu
 l1: Set Alarm
 Python:
 """
#Code
def set_alarm(employed, vacation):
    if employed == True and vacation == True:
        return False
    elif employed == True and vacation == False:
        return True
    else:
        return False
    return count
"""
8 kyu
Switch it Up!
Python:
"""
#Code
def switch_it_up(number):
    #Case to go through each number
    match number:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case 4:
            return "Four"
        case 5:
            return "Five"
        case 6: 
            return "Six"
        case 7:
            return "Seven"
        case 8:
            return "Eight"
        case 9:
            return "Nine"
"""
6 kyu
Take a Ten Minutes Walk
Python:
"""
#code
def is_valid_walk(walk):
    #Each block takes 1 minute
    #The walk needs to take exactly 10 minutes
    #Array will never be empty
    walky = len(walk)
    
    if walky != 10:
        return False
    
    x, y = 0, 0
    
    for compass in walk:
        if compass == "n":
            y += 1
        elif compass == "s":
            y -= 1
        elif compass == "e":
            x += 1
        elif compass == "w":
            x -= 1
            
    if x == 0 and y == 0:
        return True
    else:
        return False
"""
8 kyu
Total amount of points
Python:
"""
#Code
def points(games):
    points = 0
    for matches in games: 
        x, y = matches.split(":")
        if int(x) > int(y):
            points += 3
        elif int(x) < int(y): 
            points += 0
        elif int(x) == int(y):
            points += 1
        
    return points
        
        
