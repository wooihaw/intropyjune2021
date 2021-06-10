# Make a function titlecase_string that, given a string, 
# returns the a string with just the first letter made uppercase.
#
# >>>> title_case("arg")
# Arg
# >>>> title_case("python")
# Python

def title_case(string):
  # Add code here that returns the answer
  ans = string[0].upper() + string[1:]
  # ans = string.title()
  return ans
  
  
# Add print statements to check what your code does:
print(title_case("arg"))
print(title_case("python"))