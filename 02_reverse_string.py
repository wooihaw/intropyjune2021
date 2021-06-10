# Make a function reverse_string that, given a string, 
# returns that string in reverse
#
# >>>> reverse_string("arg")
# gra
# >>>> reverse_string("Hi!")
# !iH

def reverse_string(string):
  # Add code here that returns the answer
  ans = string[::-1]
  return ans
  
# Add print statements here to test what your code does:
print(reverse_string("arg"))
print(reverse_string("Hi!"))