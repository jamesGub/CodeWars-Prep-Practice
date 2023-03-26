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
        
