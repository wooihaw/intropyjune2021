# Make a function switch_case that, given a string, 
# returns the string with uppercase letters in lowercase
# and vice-versa. Include punction and other non-cased 
# characters unchanged.
#
# >>>> switch_case("Arg!")
# aRG!
# >>>> switch_case("PyThoN")
# pYtHOn

def switch_case(string):
  # Add code here that returns the answer
  ans = string.swapcase()
  return ans
  
# Add print statements to check what your code does:
print(switch_case("Arg!"))
print(switch_case("PyThoN"))