
""" Write a function called count characters that takes a string as input and returns a dictionary 
containing the count of each character in the string. The keys of the dictionary should be the characters,
and the values should be the number of times each character appears. For example, given the input 
"hello world", the function should return {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}."""

from collections import Counter

def count_character():
     
     char_count=Counter(input_str)
     return dict(char_count)
     

input_str="Hello"
result=count_character(input_str)

print(result)